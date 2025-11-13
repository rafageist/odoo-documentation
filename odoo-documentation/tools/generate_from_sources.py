#!/usr/bin/env python
import argparse
import ast
import csv
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


def read_env_or_arg(name: str, arg: Optional[str]) -> Optional[Path]:
    val = arg or os.environ.get(name)
    return Path(val) if val else None


def is_module_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    return (path / "__manifest__.py").exists() or (path / "__openerp__.py").exists()


def parse_manifest(manifest_path: Path) -> Dict:
    try:
        text = manifest_path.read_text(encoding="utf-8")
        node = ast.parse(text, filename=str(manifest_path))
        # Expect a single dict literal assigned to something or returned
        # Fallback: literal_eval on the first dict literal
        class DictVisitor(ast.NodeVisitor):
            def __init__(self):
                self.dict_node = None

            def visit_Dict(self, node: ast.Dict):
                if self.dict_node is None:
                    self.dict_node = node

        visitor = DictVisitor()
        visitor.visit(node)
        if visitor.dict_node is None:
            return {}
        data = ast.literal_eval(visitor.dict_node)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


class Relation:
    def __init__(self, field: str, kind: str, target: Optional[str]):
        self.field = field
        self.kind = kind  # many2one, one2many, many2many
        self.target = target


class ModelInfo:
    def __init__(self, py_class: str, model_name: Optional[str], inherits: List[str], relations: List[Relation]):
        self.py_class = py_class
        self.model_name = model_name
        self.inherits = inherits
        self.relations = relations


FIELD_RELATIONS = {
    "Many2one": "many2one",
    "One2many": "one2many",
    "Many2many": "many2many",
}


def _is_models_model(base: ast.AST) -> bool:
    if isinstance(base, ast.Attribute) and isinstance(base.value, ast.Name):
        return base.value.id == "models" and base.attr == "Model"
    if isinstance(base, ast.Name) and base.id == "Model":
        return True
    return False


def _const_str(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Str):  # py<3.8
        return node.s
    return None


def _call_is_fields(call: ast.Call, kinds: List[str]) -> Optional[str]:
    # fields.<Kind>(...)
    if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Name) and call.func.value.id == "fields":
        if call.func.attr in kinds:
            return call.func.attr
    return None


def parse_model_file(py_path: Path) -> List[ModelInfo]:
    infos: List[ModelInfo] = []
    try:
        text = py_path.read_text(encoding="utf-8", errors="ignore")
        node = ast.parse(text, filename=str(py_path))
        for child in node.body:
            if isinstance(child, ast.ClassDef):
                if not any(_is_models_model(b) for b in child.bases):
                    continue
                model_name: Optional[str] = None
                inherits: List[str] = []
                relations: List[Relation] = []
                for stmt in child.body:
                    if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
                        # _name or _inherit
                        if isinstance(stmt.targets[0], ast.Name):
                            tname = stmt.targets[0].id
                            if tname == "_name":
                                mn = _const_str(stmt.value)
                                if mn:
                                    model_name = mn
                            elif tname == "_inherit":
                                if isinstance(stmt.value, (ast.List, ast.Tuple)):
                                    vals: List[str] = []
                                    for elt in stmt.value.elts:
                                        cs = _const_str(elt)
                                        if cs:
                                            vals.append(cs)
                                    inherits.extend(vals)
                                else:
                                    cs = _const_str(stmt.value)
                                    if cs:
                                        inherits.append(cs)
                            else:
                                # field assignment
                                if isinstance(stmt.value, ast.Call):
                                    kind = _call_is_fields(stmt.value, list(FIELD_RELATIONS.keys()))
                                    if kind:
                                        target: Optional[str] = None
                                        # comodel is first arg or keyword comodel_name
                                        if stmt.value.args:
                                            target = _const_str(stmt.value.args[0])
                                        if not target and stmt.value.keywords:
                                            for kw in stmt.value.keywords:
                                                if kw.arg == "comodel_name":
                                                    target = _const_str(kw.value)
                                        relations.append(Relation(stmt.targets[0].id, FIELD_RELATIONS[kind], target))
                infos.append(ModelInfo(child.name, model_name, inherits, relations))
    except Exception:
        pass
    return infos


def scan_models(module_dir: Path) -> List[ModelInfo]:
    models_dir = module_dir / "models"
    found: List[ModelInfo] = []
    py_files: List[Path] = []
    if models_dir.exists():
        py_files.extend(models_dir.rglob("*.py"))
    else:
        py_files.extend(module_dir.glob("*.py"))
    for f in py_files:
        found.extend(parse_model_file(f))
    # de-dup by (py_class, model_name)
    seen: set = set()
    unique: List[ModelInfo] = []
    for mi in found:
        key = (mi.py_class, mi.model_name)
        if key not in seen:
            seen.add(key)
            unique.append(mi)
    return unique


def _localname(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def parse_xml_file(xml_path: Path) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "views": [],
        "actions": [],
        "menus": [],
        "rules": [],
    }
    try:
        import xml.etree.ElementTree as ET
        text = xml_path.read_text(encoding="utf-8", errors="ignore")
        # avoid DOCTYPE issues
        text = text.replace("<!DOCTYPE", "<!-- DOCTYPE").replace("]>", "]> -->")
        root = ET.fromstring(text)
        stack = [root]
        # Flatten iteration
        while stack:
            el = stack.pop()
            for child in list(el):
                stack.append(child)
            tag = _localname(el.tag)
            if tag == "record":
                model = el.attrib.get("model")
                rec_id = el.attrib.get("id")
                if model == "ir.ui.view":
                    vtype = None
                    vname = None
                    for f in el:
                        if _localname(f.tag) == "field":
                            n = f.attrib.get("name")
                            if n == "type":
                                vtype = (f.text or "").strip()
                            if n == "name":
                                vname = (f.text or "").strip()
                    out["views"].append({"id": rec_id, "type": vtype, "name": vname})
                elif model and model.startswith("ir.actions"):
                    atype = model.split(".")[-1]
                    aname = None
                    for f in el:
                        if _localname(f.tag) == "field" and f.attrib.get("name") == "name":
                            aname = (f.text or "").strip()
                    out["actions"].append({"id": rec_id, "type": atype, "name": aname})
                elif model == "ir.ui.menu":
                    mname = None
                    for f in el:
                        if _localname(f.tag) == "field" and f.attrib.get("name") == "name":
                            mname = (f.text or "").strip()
                    out["menus"].append({"id": rec_id, "name": mname})
                elif model == "ir.rule":
                    out["rules"].append({"id": rec_id})
            elif tag == "menuitem":
                mid = el.attrib.get("id")
                name = el.attrib.get("name")
                out["menus"].append({"id": mid, "name": name})
            elif tag == "act_window":
                aid = el.attrib.get("id")
                name = el.attrib.get("name")
                out["actions"].append({"id": aid, "type": "act_window", "name": name})
    except Exception:
        pass
    return out


def scan_xml(module_dir: Path) -> Dict[str, Any]:
    merged: Dict[str, Any] = {"views": [], "actions": [], "menus": [], "rules": [], "access": 0}
    for f in module_dir.rglob("*.xml"):
        # skip translations and docs
        if any(part in ("i18n", "tests", "test", "doc", "docs") for part in f.parts):
            continue
        data = parse_xml_file(f)
        for k in ("views", "actions", "menus", "rules"):
            merged[k].extend(data.get(k, []))
    # count access CSV
    acc_csv = module_dir / "security" / "ir.model.access.csv"
    if acc_csv.exists():
        try:
            with acc_csv.open("r", encoding="utf-8", errors="ignore") as fh:
                reader = csv.reader(fh)
                rows = list(reader)
                merged["access"] = max(0, len(rows) - 1) if rows else 0
        except Exception:
            pass
    return merged


def puml_alias(name: str) -> str:
    return name.replace(".", "_").replace("-", "_")


def compute_output_path(version_label: str, category_label: str, module_name: str, vault_root: Path) -> Path:
    base = vault_root / f"Odoo {version_label}" / f"{category_label}"
    # Write module note as <module>/<module>.md instead of README.md
    return base / module_name / f"{module_name}.md"


def ensure_dir(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)


def write_module_note(
    path: Path,
    metadata: Dict,
    module_dir: Path,
    version_tag: str,
    category_tag: str,
    source_label: str,
    source_base: Optional[Path],
    dep_links: Optional[List[str]] = None,
    rev_dep_links: Optional[List[str]] = None,
    overwrite: bool = False,
):
    name = metadata.get("name") or module_dir.name
    summary = metadata.get("summary") or ""
    depends_raw = metadata.get("depends") or []
    model_infos = scan_models(module_dir)
    xml_info = scan_xml(module_dir)
    fm_tags = ["odoo", version_tag, category_tag, "module"]
    content = []
    content.append("---")
    content.append(f"tags: [{', '.join(fm_tags)}]")
    content.append("---\n")
    content.append(f"# {name}\n")
    content.append(f"- Version: {version_tag}")
    content.append(f"- Category: {category_tag}")
    # Prefer repository-relative source reference, avoid absolute local paths
    rel_str = None
    try:
        if source_base and module_dir.resolve().is_relative_to(source_base.resolve()):
            rel_str = module_dir.resolve().relative_to(source_base.resolve()).as_posix()
    except Exception:
        try:
            # Python <3.9 compatibility: manual check
            p_res = module_dir.resolve()
            b_res = source_base.resolve() if source_base else None
            if b_res and str(p_res).startswith(str(b_res)):
                rel_str = p_res.as_posix().replace(b_res.as_posix().rstrip('/') + '/', '')
        except Exception:
            rel_str = None
    if rel_str:
        content.append(f"- Source: {source_label}/{rel_str}")
    else:
        content.append(f"- Source: {source_label}")
    # Dependencies inline (as links when available)
    if dep_links is not None:
        if dep_links:
            content.append(f"- Dependencies: {', '.join(dep_links)}")
        else:
            content.append(f"- Dependencies: none")
    elif depends_raw:
        content.append(f"- Dependencies: {', '.join(depends_raw)}")
    if summary:
        content.append("\n## Summary\n")
        content.append(summary + "\n")
    # XML artifacts summary
    content.append("## XML Artifacts (detected)\n")
    vcount = len(xml_info.get("views", []))
    acount = len(xml_info.get("actions", []))
    mcount = len(xml_info.get("menus", []))
    rcount = len(xml_info.get("rules", []))
    acc = xml_info.get("access", 0)
    content.append(f"- Views: {vcount}")
    content.append(f"- Actions: {acount}")
    content.append(f"- Menus: {mcount}")
    content.append(f"- Rules (ir.rule): {rcount}")
    content.append(f"- Access CSV entries: {acc}\n")

    # Models + relations diagram
    if model_infos:
        content.append("## Detected Models\n")
        for mi in model_infos:
            label = mi.model_name or mi.py_class
            content.append(f"- `{label}`")
        content.append("\n")
        content.append("```plantuml")
        content.append("@startuml")
        content.append("!include ../../../Templates/DiagramStyles.puml")
        content.append(f"title {name} - Models and Relations")
        defined: set = set()
        for mi in model_infos:
            label = mi.model_name or mi.py_class
            alias = puml_alias(label)
            if label not in defined:
                if label != alias:
                    content.append(f"class \"{label}\" as {alias}")
                else:
                    content.append(f"class {alias}")
                defined.add(label)
        for mi in model_infos:
            src_label = mi.model_name or mi.py_class
            src_alias = puml_alias(src_label)
            for rel in mi.relations:
                if not rel.target:
                    continue
                tgt_label = rel.target
                tgt_alias = puml_alias(tgt_label)
                if tgt_label not in defined:
                    if tgt_label != tgt_alias:
                        content.append(f"class \"{tgt_label}\" as {tgt_alias}")
                    else:
                        content.append(f"class {tgt_alias}")
                    defined.add(tgt_label)
                arrow = "-->" if rel.kind == "many2one" else "--|>" if rel.kind == "one2many" else ".."  # stylistic
                content.append(f"{src_alias} {arrow} {tgt_alias} : {rel.kind}")
        content.append("@enduml")
        content.append("```\n")
    # Dependencies links
    # Do not append dependency sections/graph at the end per request

    content.append("## Navigation\n")
    try:
        # Compose links to sibling indexes named after their folders
        mod_dir = path.parent
        cat_dir = mod_dir.parent
        ver_dir = cat_dir.parent
        content.append(f"- [[../{cat_dir.name}/{cat_dir.name}|Back to category]]")
        content.append(f"- [[../../{ver_dir.name}/{ver_dir.name}|Back to version]]\n")
    except Exception:
        content.append("- [[../|Back to category]]")
        content.append("- [[../../|Back to version]]\n")

    ensure_dir(path)
    marker = "<!-- GENERATED:MODULE -->"
    generated = "\n".join([marker] + content + [marker, ""])
    if overwrite or not path.exists():
        path.write_text(generated, encoding="utf-8")
    else:
        existing = path.read_text(encoding="utf-8", errors="ignore")
        if marker in existing:
            pre, _, rest = existing.partition(marker)
            _, _, post = rest.partition(marker)
            path.write_text(pre + generated + post, encoding="utf-8")
        else:
            # append generated section
            path.write_text(existing + ("\n" if not existing.endswith("\n") else "") + generated, encoding="utf-8")


def scan_addons(addons_root: Path) -> List[Path]:
    if not addons_root or not addons_root.exists():
        return []
    mods: List[Path] = []
    for p in addons_root.iterdir():
        if is_module_dir(p):
            mods.append(p)
    return mods


def default_paths(cwd: Path) -> Dict[str, Optional[Path]]:
    # User hint: odoo (CE18), odoo19 (CE19), enterprise18, enterprise19
    odoo18_root = cwd / "odoo"
    odoo19_root = cwd / "odoo19"
    ent18_root = cwd / "enterprise18"
    ent19_root = cwd / "enterprise19"
    return {
        "o18": odoo18_root if odoo18_root.exists() else None,
        "o19": odoo19_root if odoo19_root.exists() else None,
        "o18c": (odoo18_root / "addons") if (odoo18_root / "addons").exists() else None,
        "o19c": (odoo19_root / "addons") if (odoo19_root / "addons").exists() else None,
        "o18e": ent18_root if ent18_root.exists() else None,
        "o19e": ent19_root if ent19_root.exists() else None,
    }


def link_target(version_label: str, category_label: str, module_name: str) -> str:
    return f"Odoo {version_label}/{category_label}/{module_name}/{module_name}"


def build_dep_graph_puml(module_name: str, version_label: str, deps: List[str], revs: List[str]) -> List[str]:
    lines: List[str] = []
    lines.append("```plantuml")
    lines.append("@startuml")
    lines.append("!include ../../../Templates/DiagramStyles.puml")
    lines.append("skinparam linetype ortho")
    center = module_name
    lines.append(f"component \"{center}\" as C")
    # clusters for deps and dependents
    if deps:
        lines.append("package \"Dependencies\" {")
        for i, d in enumerate(sorted(set(deps))):
            alias = f"D{i}"
            lines.append(f"component \"{d}\" as {alias}")
            lines.append(f"C ..> {alias}")
        lines.append("}")
    if revs:
        lines.append("package \"Dependents\" {")
        for i, r in enumerate(sorted(set(revs))):
            alias = f"R{i}"
            lines.append(f"component \"{r}\" as {alias}")
            lines.append(f"{alias} ..> C")
        lines.append("}")
    lines.append("@enduml")
    lines.append("```")
    return lines


# ---- Category grouping ----

def _norm(s: str) -> str:
    return (s or "").strip().lower()


def categorize_module(mod_name: str, meta: Dict) -> str:
    n = _norm(mod_name)
    cat = _norm(meta.get("category"))
    # Primary heuristics by name prefix
    if n.startswith("l10n_"):
        return "Localizations"
    if n.startswith("account") or n in {"analytic"}:
        return "Finance"
    if n.startswith("payment_"):
        return "Payments"
    if n.startswith("pos_"):
        return "Point of Sale"
    if n.startswith("sale") or n in {"crm"} or n.startswith("coupon"):
        return "Sales"
    if n.startswith("stock") or n.startswith("mrp") or n.startswith("purchase") or n.startswith("repair") or n.startswith("maintenance"):
        return "Inventory"
    if n == "hr" or n.startswith("hr_"):
        return "HR"
    if n.startswith("marketing_") or n in {"utm", "mass_mailing"}:
        return "Marketing"
    if n.startswith("project") or n.startswith("timesheet") or n.startswith("helpdesk") or n.startswith("planning"):
        return "Services"
    if n.startswith("website") or n in {"portal", "website_slides", "website_livechat"}:
        return "Website"
    if n.startswith("mail") or n in {"bus", "im_livechat", "discuss"}:
        return "Communication"
    if n.startswith("iot_") or n.startswith("hw_"):
        return "IoT"
    if n in {"base", "base_setup", "web", "web_tour", "web_editor", "html_editor"} or n.startswith("web_"):
        return "Technical"
    # Fallback to manifest category coarse mapping
    if cat:
        if "account" in cat or "finance" in cat:
            return "Finance"
        if "sale" in cat:
            return "Sales"
        if "inventory" in cat or "stock" in cat or "manufacturing" in cat:
            return "Inventory"
        if "human resources" in cat or cat.startswith("hr"):
            return "HR"
        if "marketing" in cat:
            return "Marketing"
        if "website" in cat:
            return "Website"
        if "productivity" in cat or "services" in cat:
            return "Services"
        if "localization" in cat:
            return "Localizations"
    return "Misc"


def write_category_note(out_root: Path, version_label: str, cat_label: str, group: str, module_names: List[str]):
    base_dir = out_root / f"Odoo {version_label}" / cat_label / group
    base_dir.mkdir(parents=True, exist_ok=True)
    note = base_dir / f"{group}.md"
    lines: List[str] = []
    lines.append("---")
    lines.append(f"tags: [odoo, v{version_label}, {'community' if cat_label.startswith('Community') else 'enterprise'}, index, category]")
    lines.append("---\n")
    lines.append(f"# {group}\n")
    lines.append(f"Modules: {len(module_names)}\n")
    for m in sorted(module_names):
        link = f"[[{link_target(version_label, cat_label, m)}|{m}]]"
        lines.append(f"- {link}")
    marker = "<!-- GENERATED:CATEGORY -->"
    payload = "\n".join([marker] + lines + [marker, ""])
    # Replace or create
    if note.exists():
        existing = note.read_text(encoding="utf-8", errors="ignore")
        if marker in existing:
            pre, _, rest = existing.partition(marker)
            _, _, post = rest.partition(marker)
            note.write_text(pre + payload + post, encoding="utf-8")
        else:
            note.write_text(existing + ("\n" if not existing.endswith("\n") else "") + payload, encoding="utf-8")
    else:
        note.write_text(payload, encoding="utf-8")


def update_category_index(out_root: Path, version_label: str, cat_label: str, groups: Dict[str, List[str]]):
    idx = out_root / f"Odoo {version_label}" / cat_label / f"{cat_label}.md"
    if not idx.exists():
        return
    items = []
    for g, mods in sorted(groups.items()):
        items.append(f"- [[Odoo {version_label}/{cat_label}/{g}/{g}|{g}]] ({len(mods)})")
    block = ["## Categories\n"] + items + [""]
    marker = "<!-- GENERATED:CATEGORIES -->"
    content = idx.read_text(encoding="utf-8", errors="ignore") if idx.exists() else ""
    payload = "\n".join([marker] + block + [marker, ""])
    if marker in content:
        pre, _, rest = content.partition(marker)
        _, _, post = rest.partition(marker)
        newc = pre + payload + post
    else:
        newc = content + ("\n" if not content.endswith("\n") else "") + payload
    idx.write_text(newc, encoding="utf-8")


def write_module_changes(out_root: Path, set18: List[Path], set19: List[Path], category: str):
    out_file = out_root / "Comparisons" / "Modules Changes.md"
    name18 = {p.name for p in set18}
    name19 = {p.name for p in set19}
    nuevos = sorted(list(name19 - name18))
    deprecados = sorted(list(name18 - name19))
    # naive placeholder for renames
    renombrados: List[str] = []
    try:
        text = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
    except Exception:
        text = ""
    block = []
    block.append(f"## {category}\n")
    block.append(f"- New: {len(nuevos)}")
    for n in nuevos[:50]:
        block.append(f"  - {n}")
    block.append(f"- Deprecated: {len(deprecados)}")
    for d in deprecados[:50]:
        block.append(f"  - {d}")
    block.append(f"- Renamed: {len(renombrados)}\n")
    marker = f"<!-- COMPARE:{category} -->"
    out = text
    if marker in text:
        pre, _, post = text.partition(marker)
        out = pre + marker + "\n" + "\n".join(block) + "\n" + marker + post.split(marker, 1)[-1]
    else:
        out = text + ("\n\n" if text else "") + marker + "\n" + "\n".join(block) + "\n" + marker + "\n"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(out, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Generate Obsidian notes from Odoo sources")
    ap.add_argument("--o18")
    ap.add_argument("--o19")
    ap.add_argument("--o18c")
    ap.add_argument("--o18e")
    ap.add_argument("--o19c")
    ap.add_argument("--o19e")
    ap.add_argument("--output", default=str(Path(__file__).resolve().parents[1]))
    ap.add_argument("--scan", action="store_true", help="Scan and generate module stubs")
    ap.add_argument("--compare", action="store_true", help="Update comparison notes (modules changes)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite module notes instead of appending")
    args = ap.parse_args()

    out_root = Path(args.output)

    cfg = default_paths(Path.cwd())
    # env/args override defaults
    overrides = {
        "o18": read_env_or_arg("ODOO18_PATH", args.o18),
        "o19": read_env_or_arg("ODOO19_PATH", args.o19),
        "o18c": read_env_or_arg("ODOO18_COMMUNITY_ADDONS", args.o18c),
        "o18e": read_env_or_arg("ODOO18_ENTERPRISE_ADDONS", args.o18e),
        "o19c": read_env_or_arg("ODOO19_COMMUNITY_ADDONS", args.o19c),
        "o19e": read_env_or_arg("ODOO19_ENTERPRISE_ADDONS", args.o19e),
    }
    for k, v in overrides.items():
        if v is not None:
            cfg[k] = v

    if args.scan:
        # First pass: collect modules and manifests
        sets: Dict[str, List[Path]] = {}
        entries: List[Dict[str, Any]] = []
        for label, addons_dir, cat in [
            ("18", cfg.get("o18c"), "Community Addons"),
            ("18", cfg.get("o18e"), "Enterprise Addons"),
            ("19", cfg.get("o19c"), "Community Addons"),
            ("19", cfg.get("o19e"), "Enterprise Addons"),
        ]:
            if not addons_dir:
                continue
            modules = scan_addons(addons_dir)
            sets[f"{label}:{cat}"] = modules
            for mod_path in modules:
                manifest_path = (mod_path / "__manifest__.py") if (mod_path / "__manifest__.py").exists() else (mod_path / "__openerp__.py")
                meta = parse_manifest(manifest_path) if manifest_path and manifest_path.exists() else {}
                entries.append({
                    "label": label,
                    "category": cat,
                    "name": mod_path.name,
                    "path": mod_path,
                    "meta": meta,
                })

        # Build module lookup per version to resolve dependency links
        by_version: Dict[str, Dict[str, str]] = {"18": {}, "19": {}}
        for e in entries:
            by_version[e["label"]][e["name"]] = e["category"]

        # Build reverse dependency index per version
        rev_index: Dict[str, Dict[str, List[str]]] = {"18": {}, "19": {}}
        for e in entries:
            deps = e["meta"].get("depends") or []
            for d in deps:
                if d in by_version[e["label"]]:
                    rev_index[e["label"]].setdefault(d, []).append(e["name"])

        # Group entries by semantic categories (for index notes)
        grouped: Dict[Tuple[str, str], Dict[str, List[str]]] = {}
        for e in entries:
            key = (e["label"], e["category"])
            g = categorize_module(e["name"], e["meta"])
            grouped.setdefault(key, {}).setdefault(g, []).append(e["name"]) 

        # Second pass: write notes with dependency links
        for e in entries:
            out_path = compute_output_path(e["label"], e["category"], e["name"], out_root)
            # Determine base repo label and path for relative source references
            if e["category"] == "Community Addons":
                base_label = "odoo" if e["label"] == "18" else "odoo19"
                base_path = cfg.get("o18c").parent if (e["label"] == "18" and cfg.get("o18c")) else (cfg.get("o19c").parent if cfg.get("o19c") else None)
            else:
                base_label = "enterprise18" if e["label"] == "18" else "enterprise19"
                base_path = cfg.get("o18e") if (e["label"] == "18") else cfg.get("o19e")

            # Build dependency wikilinks
            dep_links: List[str] = []
            for d in e["meta"].get("depends") or []:
                cat = by_version[e["label"]].get(d)
                if cat:
                    dep_links.append(f"[[{link_target(e['label'], cat, d)}|{d}]]")
                else:
                    dep_links.append(f"{d} (not documented)")

            # Build reverse dependency wikilinks
            rev_deps = rev_index[e["label"]].get(e["name"], [])
            rev_links: List[str] = []
            for r in sorted(set(rev_deps)):
                cat = by_version[e["label"]].get(r)
                if cat:
                    rev_links.append(f"[[{link_target(e['label'], cat, r)}|{r}]]")

            write_module_note(
                out_path,
                e["meta"],
                e["path"],
                f"v{e['label']}",
                e["category"].split()[0].lower(),
                base_label,
                base_path,
                dep_links,
                None,
                overwrite=args.overwrite,
            )

        # Write category notes and update category indices
        for (lbl, catlbl), groups in grouped.items():
            for gname, mods in groups.items():
                write_category_note(out_root, lbl, catlbl, gname, mods)
            update_category_index(out_root, lbl, catlbl, groups)

        # optional comparisons
        if args.compare:
            if sets.get("18:Community Addons") and sets.get("19:Community Addons"):
                write_module_changes(out_root, sets["18:Community Addons"], sets["19:Community Addons"], "Community Addons")
            if sets.get("18:Enterprise Addons") and sets.get("19:Enterprise Addons"):
                write_module_changes(out_root, sets["18:Enterprise Addons"], sets["19:Enterprise Addons"], "Enterprise Addons")

        print("Generation finished.")
    else:
        print("Nothing to do. Use --scan and configure paths. See CONFIG.md")


if __name__ == "__main__":
    main()
