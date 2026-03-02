#!/usr/bin/env python
import argparse
import ast
import csv
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

DOCS_DIR = "docs"
DOCS_NOTE = f"{DOCS_DIR}/docs"
TEMPLATES_DIR = "templates"


def read_env_or_arg(name: str, arg: Optional[str]) -> Optional[Path]:
    value = arg or os.environ.get(name)
    return Path(value) if value else None


def discover_enterprise_root(workspace_root: Path) -> Optional[Path]:
    cache_root = workspace_root / "docker" / "odoo19-enterprise-sync" / "enterprise-cache"
    if not cache_root.exists():
        return None
    candidates = [p for p in cache_root.iterdir() if p.is_dir()]
    if not candidates:
        return None
    return sorted(candidates, key=lambda p: p.stat().st_mtime, reverse=True)[0]


def default_paths(repo_root: Path) -> Dict[str, Optional[Path]]:
    workspace_root = repo_root.parent
    odoo_root = workspace_root / "odoo19"
    enterprise_root = discover_enterprise_root(workspace_root)
    return {
        "odoo": odoo_root if odoo_root.exists() else None,
        "community": (odoo_root / "addons") if (odoo_root / "addons").exists() else None,
        "enterprise": enterprise_root,
    }


def is_module_dir(path: Path) -> bool:
    return path.is_dir() and ((path / "__manifest__.py").exists() or (path / "__openerp__.py").exists())


def parse_manifest(manifest_path: Path) -> Dict[str, Any]:
    try:
        text = manifest_path.read_text(encoding="utf-8")
        node = ast.parse(text, filename=str(manifest_path))

        class DictVisitor(ast.NodeVisitor):
            def __init__(self) -> None:
                self.dict_node = None

            def visit_Dict(self, node: ast.Dict) -> None:
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
    def __init__(self, field: str, kind: str, target: Optional[str]) -> None:
        self.field = field
        self.kind = kind
        self.target = target


class ModelInfo:
    def __init__(self, py_class: str, model_name: Optional[str], inherits: List[str], relations: List[Relation]) -> None:
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
    return isinstance(base, ast.Name) and base.id == "Model"


def _const_str(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Str):
        return node.s
    return None


def _call_is_fields(call: ast.Call, kinds: List[str]) -> Optional[str]:
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
            if not isinstance(child, ast.ClassDef):
                continue
            if not any(_is_models_model(base) for base in child.bases):
                continue
            model_name: Optional[str] = None
            inherits: List[str] = []
            relations: List[Relation] = []
            for stmt in child.body:
                if not isinstance(stmt, ast.Assign) or len(stmt.targets) != 1 or not isinstance(stmt.targets[0], ast.Name):
                    continue
                target_name = stmt.targets[0].id
                if target_name == "_name":
                    model_name = _const_str(stmt.value) or model_name
                    continue
                if target_name == "_inherit":
                    if isinstance(stmt.value, (ast.List, ast.Tuple)):
                        inherits.extend(filter(None, (_const_str(item) for item in stmt.value.elts)))
                    else:
                        inherited = _const_str(stmt.value)
                        if inherited:
                            inherits.append(inherited)
                    continue
                if isinstance(stmt.value, ast.Call):
                    kind = _call_is_fields(stmt.value, list(FIELD_RELATIONS.keys()))
                    if not kind:
                        continue
                    comodel = _const_str(stmt.value.args[0]) if stmt.value.args else None
                    if not comodel:
                        for keyword in stmt.value.keywords:
                            if keyword.arg == "comodel_name":
                                comodel = _const_str(keyword.value)
                                break
                    relations.append(Relation(target_name, FIELD_RELATIONS[kind], comodel))
            infos.append(ModelInfo(child.name, model_name, inherits, relations))
    except Exception:
        pass
    return infos


def scan_models(module_dir: Path) -> List[ModelInfo]:
    models_dir = module_dir / "models"
    py_files = list(models_dir.rglob("*.py")) if models_dir.exists() else list(module_dir.glob("*.py"))
    found: List[ModelInfo] = []
    for py_file in py_files:
        found.extend(parse_model_file(py_file))
    unique: List[ModelInfo] = []
    seen = set()
    for item in found:
        key = (item.py_class, item.model_name)
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def _localname(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def parse_xml_file(xml_path: Path) -> Dict[str, Any]:
    result: Dict[str, Any] = {"views": [], "actions": [], "menus": [], "rules": []}
    try:
        import xml.etree.ElementTree as ET

        text = xml_path.read_text(encoding="utf-8", errors="ignore")
        text = text.replace("<!DOCTYPE", "<!-- DOCTYPE").replace("]>", "]> -->")
        root = ET.fromstring(text)
        stack = [root]
        while stack:
            element = stack.pop()
            for child in list(element):
                stack.append(child)
            tag = _localname(element.tag)
            if tag == "record":
                model = element.attrib.get("model")
                record_id = element.attrib.get("id")
                if model == "ir.ui.view":
                    view_type = None
                    view_name = None
                    for field in element:
                        if _localname(field.tag) != "field":
                            continue
                        if field.attrib.get("name") == "type":
                            view_type = (field.text or "").strip()
                        if field.attrib.get("name") == "name":
                            view_name = (field.text or "").strip()
                    result["views"].append({"id": record_id, "type": view_type, "name": view_name})
                elif model and model.startswith("ir.actions"):
                    action_type = model.split(".")[-1]
                    action_name = None
                    for field in element:
                        if _localname(field.tag) == "field" and field.attrib.get("name") == "name":
                            action_name = (field.text or "").strip()
                    result["actions"].append({"id": record_id, "type": action_type, "name": action_name})
                elif model == "ir.ui.menu":
                    menu_name = None
                    for field in element:
                        if _localname(field.tag) == "field" and field.attrib.get("name") == "name":
                            menu_name = (field.text or "").strip()
                    result["menus"].append({"id": record_id, "name": menu_name})
                elif model == "ir.rule":
                    result["rules"].append({"id": record_id})
            elif tag == "menuitem":
                result["menus"].append({"id": element.attrib.get("id"), "name": element.attrib.get("name")})
            elif tag == "act_window":
                result["actions"].append({"id": element.attrib.get("id"), "type": "act_window", "name": element.attrib.get("name")})
    except Exception:
        pass
    return result


def scan_xml(module_dir: Path) -> Dict[str, Any]:
    merged: Dict[str, Any] = {"views": [], "actions": [], "menus": [], "rules": [], "access": 0}
    for xml_file in module_dir.rglob("*.xml"):
        if any(part in ("i18n", "tests", "test", "doc", "docs") for part in xml_file.parts):
            continue
        parsed = parse_xml_file(xml_file)
        for key in ("views", "actions", "menus", "rules"):
            merged[key].extend(parsed.get(key, []))
    access_file = module_dir / "security" / "ir.model.access.csv"
    if access_file.exists():
        try:
            with access_file.open("r", encoding="utf-8", errors="ignore") as handle:
                rows = list(csv.reader(handle))
                merged["access"] = max(0, len(rows) - 1)
        except Exception:
            pass
    return merged


def puml_alias(name: str) -> str:
    return name.replace(".", "_").replace("-", "_")


def scan_addons(addons_root: Path) -> List[Path]:
    if not addons_root or not addons_root.exists():
        return []
    return sorted([path for path in addons_root.iterdir() if is_module_dir(path)], key=lambda path: path.name)


def compute_output_path(scope: str, module_name: str, output_root: Path) -> Path:
    return output_root / DOCS_DIR / scope / module_name / f"{module_name}.md"


def link_target(scope: str, module_name: str) -> str:
    return f"{DOCS_DIR}/{scope}/{module_name}/{module_name}"


def ensure_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def categorize_module(module_name: str, meta: Dict[str, Any]) -> str:
    name = (module_name or "").strip().lower()
    category = (meta.get("category") or "").strip().lower()
    if name.startswith("l10n_"):
        return "Localizations"
    if name.startswith("account") or name in {"analytic"}:
        return "Finance"
    if name.startswith("payment_"):
        return "Payments"
    if name.startswith("pos_"):
        return "Point of Sale"
    if name.startswith("sale") or name in {"crm"} or name.startswith("coupon"):
        return "Sales"
    if name.startswith(("stock", "mrp", "purchase", "repair", "maintenance")):
        return "Inventory"
    if name == "hr" or name.startswith("hr_"):
        return "HR"
    if name.startswith("marketing_") or name in {"utm", "mass_mailing"}:
        return "Marketing"
    if name.startswith(("project", "timesheet", "helpdesk", "planning")):
        return "Services"
    if name.startswith("website") or name in {"portal", "website_slides", "website_livechat"}:
        return "Website"
    if name.startswith("mail") or name in {"bus", "im_livechat", "discuss"}:
        return "Communication"
    if name.startswith(("iot_", "hw_")) or name == "iot":
        return "IoT"
    if name in {"base", "base_setup", "web", "web_tour", "web_editor", "html_editor"} or name.startswith("web_"):
        return "Technical"
    if "account" in category or "finance" in category:
        return "Finance"
    if "sale" in category:
        return "Sales"
    if "inventory" in category or "stock" in category or "manufacturing" in category:
        return "Inventory"
    if "human resources" in category or category.startswith("hr"):
        return "HR"
    if "marketing" in category:
        return "Marketing"
    if "website" in category:
        return "Website"
    if "productivity" in category or "services" in category:
        return "Services"
    if "localization" in category:
        return "Localizations"
    return "Misc"


def write_module_note(
    path: Path,
    metadata: Dict[str, Any],
    module_dir: Path,
    scope: str,
    source_label: str,
    source_base: Optional[Path],
    dep_links: List[str],
    overwrite: bool = False,
) -> None:
    name = metadata.get("name") or module_dir.name
    summary = metadata.get("summary") or ""
    models = scan_models(module_dir)
    xml_info = scan_xml(module_dir)
    tags = ["odoo", "community" if scope == "Community Addons" else "enterprise", "module"]

    lines: List[str] = [
        "<!-- GENERATED:MODULE -->",
        "---",
        f"tags: [{', '.join(tags)}]",
        "---",
        "",
        f"# {name}",
        "",
        f"- Scope: {scope}",
    ]

    relative_source = None
    try:
        if source_base:
            relative_source = module_dir.resolve().relative_to(source_base.resolve()).as_posix()
    except Exception:
        relative_source = None
    lines.append(f"- Source: {source_label}/{relative_source}" if relative_source else f"- Source: {source_label}")
    lines.append(f"- Dependencies: {', '.join(dep_links) if dep_links else 'none'}")

    if summary:
        lines.extend(["", "## Summary", "", summary])

    lines.extend(
        [
            "",
            "## XML Artifacts (detected)",
            "",
            f"- Views: {len(xml_info.get('views', []))}",
            f"- Actions: {len(xml_info.get('actions', []))}",
            f"- Menus: {len(xml_info.get('menus', []))}",
            f"- Rules (ir.rule): {len(xml_info.get('rules', []))}",
            f"- Access CSV entries: {xml_info.get('access', 0)}",
        ]
    )

    if models:
        lines.extend(["", "## Detected Models", ""])
        for model in models:
            lines.append(f"- `{model.model_name or model.py_class}`")
        lines.extend(["", "```plantuml", "@startuml", f"!include ../../../{TEMPLATES_DIR}/DiagramStyles.puml", f"title {name} - Models and Relations"])
        defined = set()
        for model in models:
            label = model.model_name or model.py_class
            alias = puml_alias(label)
            if label in defined:
                continue
            lines.append(f'class "{label}" as {alias}' if alias != label else f"class {alias}")
            defined.add(label)
        for model in models:
            source_label_name = model.model_name or model.py_class
            source_alias = puml_alias(source_label_name)
            for relation in model.relations:
                if not relation.target:
                    continue
                target_alias = puml_alias(relation.target)
                if relation.target not in defined:
                    lines.append(f'class "{relation.target}" as {target_alias}' if relation.target != target_alias else f"class {target_alias}")
                    defined.add(relation.target)
                arrow = "-->" if relation.kind == "many2one" else "--|>" if relation.kind == "one2many" else ".."
                lines.append(f"{source_alias} {arrow} {target_alias} : {relation.kind}")
        lines.extend(["@enduml", "```"])

    lines.extend(
        [
            "",
            "## Navigation",
            "",
            f"- [[../{scope}/{scope}|Back to scope]]",
            f"- [[../../{DOCS_NOTE}|Back to docs]]",
            "",
            "<!-- GENERATED:MODULE -->",
            "",
        ]
    )

    content = "\n".join(lines)
    ensure_dir(path)
    if overwrite or not path.exists():
        path.write_text(content, encoding="utf-8")
        return

    existing = path.read_text(encoding="utf-8", errors="ignore")
    marker = "<!-- GENERATED:MODULE -->"
    if marker in existing:
        prefix, _, remainder = existing.partition(marker)
        _, _, suffix = remainder.partition(marker)
        path.write_text(prefix + content + suffix, encoding="utf-8")
    else:
        path.write_text(existing + ("\n" if not existing.endswith("\n") else "") + content, encoding="utf-8")


def write_category_note(output_root: Path, scope: str, category: str, module_names: List[str]) -> None:
    scope_tag = "community" if scope == "Community Addons" else "enterprise"
    note_path = output_root / DOCS_DIR / scope / category / f"{category}.md"
    lines: List[str] = [
        "---",
        f"tags: [odoo, {scope_tag}, index, category]",
        "---",
        "",
        f"# {category}",
        "",
        f"- Scope: {scope}",
        f"- Modules: {len(module_names)}",
        "",
        "## Modules",
        "",
    ]
    for module_name in sorted(module_names):
        lines.append(f"- [[{link_target(scope, module_name)}|{module_name}]]")
    lines.extend(["", "## Navigation", "", f"- [[../{scope}|Back to scope]]", f"- [[../../{DOCS_NOTE}|Back to docs]]", ""])
    ensure_dir(note_path)
    note_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate documentation notes from local Odoo sources")
    parser.add_argument("--odoo")
    parser.add_argument("--community-addons")
    parser.add_argument("--enterprise-addons")
    parser.add_argument("--output", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--scan", action="store_true", help="Scan local sources and refresh addon notes")
    parser.add_argument("--overwrite", action="store_true", help="Replace generated module sections instead of appending them")
    args = parser.parse_args()

    if not args.scan:
        print("Nothing to do. Use --scan. See CONFIG.md")
        return

    output_root = Path(args.output)
    config = default_paths(output_root)
    overrides = {
        "odoo": read_env_or_arg("ODOO_PATH", args.odoo),
        "community": read_env_or_arg("ODOO_COMMUNITY_ADDONS", args.community_addons),
        "enterprise": read_env_or_arg("ODOO_ENTERPRISE_ADDONS", args.enterprise_addons),
    }
    for key, value in overrides.items():
        if value is not None:
            config[key] = value

    entries: List[Dict[str, Any]] = []
    for scope, addons_root in (("Community Addons", config.get("community")), ("Enterprise Addons", config.get("enterprise"))):
        if not addons_root:
            continue
        for module_dir in scan_addons(addons_root):
            manifest_path = module_dir / "__manifest__.py"
            if not manifest_path.exists():
                manifest_path = module_dir / "__openerp__.py"
            metadata = parse_manifest(manifest_path) if manifest_path.exists() else {}
            entries.append({"scope": scope, "name": module_dir.name, "path": module_dir, "meta": metadata})

    scope_lookup: Dict[str, Dict[str, str]] = {"Community Addons": {}, "Enterprise Addons": {}}
    for entry in entries:
        scope_lookup[entry["scope"]][entry["name"]] = entry["scope"]

    grouped: Dict[str, Dict[str, List[str]]] = {"Community Addons": {}, "Enterprise Addons": {}}
    for entry in entries:
        category = categorize_module(entry["name"], entry["meta"])
        grouped[entry["scope"]].setdefault(category, []).append(entry["name"])

    for entry in entries:
        scope = entry["scope"]
        module_dir = entry["path"]
        output_path = compute_output_path(scope, entry["name"], output_root)
        source_label = "odoo" if scope == "Community Addons" else "enterprise"
        source_base = config.get("odoo") if scope == "Community Addons" else config.get("enterprise")
        dep_links: List[str] = []
        for dependency in entry["meta"].get("depends") or []:
            dependency_scope = scope_lookup["Community Addons"].get(dependency) or scope_lookup["Enterprise Addons"].get(dependency)
            if dependency_scope:
                dep_links.append(f"[[{link_target(dependency_scope, dependency)}|{dependency}]]")
            else:
                dep_links.append(f"{dependency} (not documented)")
        write_module_note(output_path, entry["meta"], module_dir, scope, source_label, source_base, dep_links, overwrite=args.overwrite)

    for scope, categories in grouped.items():
        for category, module_names in categories.items():
            write_category_note(output_root, scope, category, module_names)

    print("Generation finished.")


if __name__ == "__main__":
    main()
