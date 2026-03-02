#!/usr/bin/env python
import argparse
import ast
import csv
import os
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

DOCS_DIR = "docs"
DOCS_NOTE = f"{DOCS_DIR}/docs"
TEMPLATES_DIR = "templates"
MODEL_SECTION = "Models"
VIEW_SECTION = "Views"
CONTROLLER_SECTION = "Controllers"
FRONTEND_SECTION = "Frontend"

FRONTEND_EXTENSIONS = {".js", ".ts", ".xml"}
REGISTRY_RE = re.compile(r"registry\.category\((['\"])([^'\"]+)\1\)\.add\((['\"])([^'\"]+)\3")
COMPONENT_RE = re.compile(r"class\s+([A-Za-z_][A-Za-z0-9_]*)\s+extends\s+([A-Za-z0-9_.]+)")
TEMPLATE_RE = re.compile(r't-name=(["\'])([^"\']+)\1')


def read_env_or_arg(name: str, arg: Optional[str]) -> Optional[Path]:
    value = arg or os.environ.get(name)
    return Path(value) if value else None


def discover_enterprise_root(workspace_root: Path) -> Optional[Path]:
    cache_root = workspace_root / "docker" / "odoo19-enterprise-sync" / "enterprise-cache"
    if not cache_root.exists():
        return None
    candidates = [path for path in cache_root.iterdir() if path.is_dir()]
    if not candidates:
        return None
    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)[0]


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

            def visit_Dict(self, current: ast.Dict) -> None:
                if self.dict_node is None:
                    self.dict_node = current

        visitor = DictVisitor()
        visitor.visit(node)
        if visitor.dict_node is None:
            return {}
        data = ast.literal_eval(visitor.dict_node)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def ensure_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    cleaned = cleaned.strip("._")
    return cleaned or "note"


def _localname(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def _const_str(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _const_bool(node: ast.AST) -> Optional[bool]:
    if isinstance(node, ast.Constant) and isinstance(node.value, bool):
        return node.value
    return None


def _expr_text(node: ast.AST) -> str:
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def _list_of_str(node: ast.AST) -> List[str]:
    if isinstance(node, (ast.List, ast.Tuple)):
        return [item for element in node.elts if (item := _const_str(element))]
    item = _const_str(node)
    return [item] if item else []


def _decorator_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Call):
        return _decorator_name(node.func)
    return ""


def _is_models_model(base: ast.AST) -> bool:
    if isinstance(base, ast.Attribute) and isinstance(base.value, ast.Name):
        return base.value.id == "models" and base.attr in {"Model", "TransientModel", "AbstractModel"}
    return isinstance(base, ast.Name) and base.id in {"Model", "TransientModel", "AbstractModel"}


def relative_source(path: Path, base: Path) -> str:
    try:
        return path.resolve().relative_to(base.resolve()).as_posix()
    except Exception:
        return path.as_posix()


@dataclass
class Relation:
    field: str
    kind: str
    target: Optional[str]


@dataclass
class FieldInfo:
    name: str
    field_type: str
    source_file: str
    comodel_name: Optional[str] = None
    related: Optional[str] = None
    compute: Optional[str] = None
    store: Optional[bool] = None


@dataclass
class MethodInfo:
    name: str
    decorators: List[str]
    source_file: str


@dataclass
class ModelBucket:
    model_name: str
    source_files: set[str] = field(default_factory=set)
    python_classes: set[str] = field(default_factory=set)
    inherits: set[str] = field(default_factory=set)
    fields: Dict[str, FieldInfo] = field(default_factory=dict)
    relations: Dict[tuple[str, str, str], Relation] = field(default_factory=dict)
    methods: Dict[str, MethodInfo] = field(default_factory=dict)
    defined_in_module: bool = False
    description: Optional[str] = None


@dataclass
class ViewRecord:
    xml_id: str
    name: Optional[str]
    model_name: Optional[str]
    view_type: Optional[str]
    inherit_id: Optional[str]
    root_tag: Optional[str]
    field_names: List[str]
    button_names: List[str]
    xpath_count: int


@dataclass
class XmlFileInfo:
    note_name: str
    source_file: str
    views: List[ViewRecord] = field(default_factory=list)
    actions: List[Dict[str, Optional[str]]] = field(default_factory=list)
    menus: List[Dict[str, Optional[str]]] = field(default_factory=list)
    rules: List[Dict[str, Optional[str]]] = field(default_factory=list)


@dataclass
class XmlScanResult:
    files: List[XmlFileInfo] = field(default_factory=list)
    access_entries: int = 0

    @property
    def view_count(self) -> int:
        return sum(len(item.views) for item in self.files)

    @property
    def action_count(self) -> int:
        return sum(len(item.actions) for item in self.files)

    @property
    def menu_count(self) -> int:
        return sum(len(item.menus) for item in self.files)

    @property
    def rule_count(self) -> int:
        return sum(len(item.rules) for item in self.files)


@dataclass
class RouteInfo:
    method_name: str
    paths: List[str]
    route_type: Optional[str]
    auth: Optional[str]
    website: Optional[bool]
    readonly: Optional[str]


@dataclass
class ControllerInfo:
    note_name: str
    title: str
    source_file: str
    base_classes: List[str]
    routes: List[RouteInfo] = field(default_factory=list)


@dataclass
class FrontendAssetInfo:
    note_name: str
    source_file: str
    asset_kind: str
    component_classes: List[str] = field(default_factory=list)
    registry_entries: List[str] = field(default_factory=list)
    templates: List[str] = field(default_factory=list)


@dataclass
class ModuleAnalysis:
    scope: str
    module_name: str
    module_dir: Path
    metadata: Dict[str, Any]
    models: List[ModelBucket]
    xml: XmlScanResult
    controllers: List[ControllerInfo]
    frontend_assets: List[FrontendAssetInfo]


FIELD_RELATIONS = {
    "Many2one": "many2one",
    "One2many": "one2many",
    "Many2many": "many2many",
}


def parse_model_file(module_dir: Path, py_path: Path, buckets: Dict[str, ModelBucket]) -> None:
    try:
        text = py_path.read_text(encoding="utf-8", errors="ignore")
        node = ast.parse(text, filename=str(py_path))
    except Exception:
        return

    source_file = relative_source(py_path, module_dir)
    for child in node.body:
        if not isinstance(child, ast.ClassDef):
            continue
        if not any(_is_models_model(base) for base in child.bases):
            continue

        model_name: Optional[str] = None
        inherits: List[str] = []
        description: Optional[str] = None
        fields: List[FieldInfo] = []
        relations: List[Relation] = []
        methods: List[MethodInfo] = []

        for stmt in child.body:
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
                target_name = stmt.targets[0].id
                if target_name == "_name":
                    model_name = _const_str(stmt.value) or model_name
                    continue
                if target_name == "_inherit":
                    inherits.extend(_list_of_str(stmt.value))
                    continue
                if target_name == "_description":
                    description = _const_str(stmt.value) or description
                    continue
                if isinstance(stmt.value, ast.Call):
                    field_call = stmt.value
                    if isinstance(field_call.func, ast.Attribute) and isinstance(field_call.func.value, ast.Name) and field_call.func.value.id == "fields":
                        field_type = field_call.func.attr
                        comodel_name = _const_str(field_call.args[0]) if field_call.args else None
                        related = None
                        compute = None
                        store = None
                        if not comodel_name:
                            for keyword in field_call.keywords:
                                if keyword.arg == "comodel_name":
                                    comodel_name = _const_str(keyword.value)
                        for keyword in field_call.keywords:
                            if keyword.arg == "related":
                                related = _const_str(keyword.value)
                            elif keyword.arg == "compute":
                                compute = _const_str(keyword.value)
                            elif keyword.arg == "store":
                                store = _const_bool(keyword.value)
                        fields.append(
                            FieldInfo(
                                name=target_name,
                                field_type=field_type,
                                source_file=source_file,
                                comodel_name=comodel_name,
                                related=related,
                                compute=compute,
                                store=store,
                            )
                        )
                        if field_type in FIELD_RELATIONS:
                            relations.append(Relation(target_name, FIELD_RELATIONS[field_type], comodel_name))
            elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.append(
                    MethodInfo(
                        name=stmt.name,
                        decorators=[name for deco in stmt.decorator_list if (name := _decorator_name(deco))],
                        source_file=source_file,
                    )
                )

        effective_models: List[str] = []
        if model_name:
            effective_models.append(model_name)
        elif inherits:
            effective_models.extend(inherits)
        if not effective_models:
            continue

        for effective_model in effective_models:
            bucket = buckets.setdefault(effective_model, ModelBucket(model_name=effective_model))
            bucket.source_files.add(source_file)
            bucket.python_classes.add(child.name)
            bucket.inherits.update(item for item in inherits if item != effective_model)
            if model_name == effective_model:
                bucket.defined_in_module = True
            if description and not bucket.description:
                bucket.description = description
            for field_info in fields:
                bucket.fields.setdefault(field_info.name, field_info)
            for relation in relations:
                key = (relation.field, relation.kind, relation.target or "")
                bucket.relations.setdefault(key, relation)
            for method in methods:
                bucket.methods.setdefault(method.name, method)


def scan_models(module_dir: Path) -> List[ModelBucket]:
    buckets: Dict[str, ModelBucket] = {}
    for py_file in sorted(module_dir.rglob("*.py")):
        if any(part in {"tests", "test", "__pycache__"} for part in py_file.parts):
            continue
        parse_model_file(module_dir, py_file, buckets)
    return sorted(buckets.values(), key=lambda item: item.model_name)


def _parse_arch_field(field_node: ET.Element) -> tuple[Optional[str], List[str], List[str], int]:
    root_tag = None
    field_names: set[str] = set()
    button_names: set[str] = set()
    xpath_count = 0

    if list(field_node):
        arch_nodes = list(field_node)
    else:
        arch_text = (field_node.text or "").strip()
        if not arch_text:
            return None, [], [], 0
        try:
            arch_nodes = [ET.fromstring(arch_text)]
        except Exception:
            return None, [], [], 0

    if arch_nodes:
        root_tag = _localname(arch_nodes[0].tag)

    for arch_node in arch_nodes:
        for current in arch_node.iter():
            tag = _localname(current.tag)
            if tag == "field" and current.attrib.get("name"):
                field_names.add(current.attrib["name"])
            elif tag == "button" and current.attrib.get("name"):
                button_names.add(current.attrib["name"])
            elif tag == "xpath":
                xpath_count += 1
            elif current.attrib.get("position"):
                xpath_count += 1

    return root_tag, sorted(field_names), sorted(button_names), xpath_count


def parse_xml_file(module_dir: Path, xml_path: Path) -> Optional[XmlFileInfo]:
    try:
        text = xml_path.read_text(encoding="utf-8", errors="ignore")
        text = text.replace("<!DOCTYPE", "<!-- DOCTYPE").replace("]>", "]> -->")
        root = ET.fromstring(text)
    except Exception:
        return None

    info = XmlFileInfo(
        note_name=safe_filename(relative_source(xml_path, module_dir)),
        source_file=relative_source(xml_path, module_dir),
    )
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
                view_name = None
                model_name = None
                view_type = None
                inherit_id = None
                root_tag = None
                field_names: List[str] = []
                button_names: List[str] = []
                xpath_count = 0
                for field_node in element:
                    if _localname(field_node.tag) != "field":
                        continue
                    field_name = field_node.attrib.get("name")
                    if field_name == "name":
                        view_name = (field_node.text or "").strip() or None
                    elif field_name == "model":
                        model_name = (field_node.text or "").strip() or None
                    elif field_name == "type":
                        view_type = (field_node.text or "").strip() or None
                    elif field_name == "inherit_id":
                        inherit_id = field_node.attrib.get("ref") or (field_node.text or "").strip() or None
                    elif field_name == "arch":
                        root_tag, field_names, button_names, xpath_count = _parse_arch_field(field_node)
                info.views.append(
                    ViewRecord(
                        xml_id=record_id or safe_filename(view_name or "view"),
                        name=view_name,
                        model_name=model_name,
                        view_type=view_type,
                        inherit_id=inherit_id,
                        root_tag=root_tag,
                        field_names=field_names,
                        button_names=button_names,
                        xpath_count=xpath_count,
                    )
                )
            elif model and model.startswith("ir.actions"):
                action_name = None
                for field_node in element:
                    if _localname(field_node.tag) == "field" and field_node.attrib.get("name") == "name":
                        action_name = (field_node.text or "").strip() or None
                info.actions.append({"id": record_id, "type": model.split(".")[-1], "name": action_name})
            elif model == "ir.ui.menu":
                menu_name = None
                for field_node in element:
                    if _localname(field_node.tag) == "field" and field_node.attrib.get("name") == "name":
                        menu_name = (field_node.text or "").strip() or None
                info.menus.append({"id": record_id, "name": menu_name})
            elif model == "ir.rule":
                info.rules.append({"id": record_id})
        elif tag == "menuitem":
            info.menus.append({"id": element.attrib.get("id"), "name": element.attrib.get("name")})
        elif tag == "act_window":
            info.actions.append({"id": element.attrib.get("id"), "type": "act_window", "name": element.attrib.get("name")})

    if not any((info.views, info.actions, info.menus, info.rules)):
        return None
    return info


def scan_xml(module_dir: Path) -> XmlScanResult:
    result = XmlScanResult()
    for xml_file in sorted(module_dir.rglob("*.xml")):
        if any(part in {"i18n", "tests", "test", "doc", "docs"} for part in xml_file.parts):
            continue
        parsed = parse_xml_file(module_dir, xml_file)
        if parsed:
            result.files.append(parsed)

    access_file = module_dir / "security" / "ir.model.access.csv"
    if access_file.exists():
        try:
            with access_file.open("r", encoding="utf-8", errors="ignore") as handle:
                rows = list(csv.reader(handle))
                result.access_entries = max(0, len(rows) - 1)
        except Exception:
            result.access_entries = 0
    return result


def _extract_route_info(method_name: str, decorator: ast.AST) -> Optional[RouteInfo]:
    if not isinstance(decorator, ast.Call):
        return None
    if _decorator_name(decorator) != "route":
        return None
    paths: List[str] = []
    if decorator.args:
        first_arg = decorator.args[0]
        if item := _const_str(first_arg):
            paths = [item]
        elif isinstance(first_arg, (ast.List, ast.Tuple)):
            paths = [item for element in first_arg.elts if (item := _const_str(element))]
    route_type = None
    auth = None
    website = None
    readonly = None
    for keyword in decorator.keywords:
        if keyword.arg == "type":
            route_type = _const_str(keyword.value) or _expr_text(keyword.value)
        elif keyword.arg == "auth":
            auth = _const_str(keyword.value) or _expr_text(keyword.value)
        elif keyword.arg == "website":
            website = _const_bool(keyword.value)
        elif keyword.arg == "readonly":
            readonly = _const_str(keyword.value) or _expr_text(keyword.value)
    return RouteInfo(
        method_name=method_name,
        paths=paths or ["<dynamic>"],
        route_type=route_type,
        auth=auth,
        website=website,
        readonly=readonly,
    )


def parse_controller_file(module_dir: Path, py_path: Path) -> List[ControllerInfo]:
    try:
        text = py_path.read_text(encoding="utf-8", errors="ignore")
        node = ast.parse(text, filename=str(py_path))
    except Exception:
        return []

    source_file = relative_source(py_path, module_dir)
    controllers: List[ControllerInfo] = []
    module_level_routes: List[RouteInfo] = []

    for child in node.body:
        if isinstance(child, ast.ClassDef):
            routes: List[RouteInfo] = []
            for item in child.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                for decorator in item.decorator_list:
                    route_info = _extract_route_info(item.name, decorator)
                    if route_info:
                        routes.append(route_info)
            if routes:
                controllers.append(
                    ControllerInfo(
                        note_name=safe_filename(child.name),
                        title=child.name,
                        source_file=source_file,
                        base_classes=[_expr_text(base) for base in child.bases if _expr_text(base)],
                        routes=routes,
                    )
                )
        elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in child.decorator_list:
                route_info = _extract_route_info(child.name, decorator)
                if route_info:
                    module_level_routes.append(route_info)

    if module_level_routes:
        controllers.append(
            ControllerInfo(
                note_name=safe_filename(py_path.stem),
                title=f"{py_path.stem} module routes",
                source_file=source_file,
                base_classes=[],
                routes=module_level_routes,
            )
        )
    return controllers


def scan_controllers(module_dir: Path) -> List[ControllerInfo]:
    controllers_dir = module_dir / "controllers"
    if not controllers_dir.exists():
        return []
    found: List[ControllerInfo] = []
    for py_file in sorted(controllers_dir.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        found.extend(parse_controller_file(module_dir, py_file))
    return sorted(found, key=lambda item: (item.source_file, item.title))


def parse_frontend_file(module_dir: Path, file_path: Path) -> FrontendAssetInfo:
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    source_file = relative_source(file_path, module_dir)
    rel_parts = Path(source_file).parts
    if "views" in rel_parts:
        asset_kind = "view"
    elif "components" in rel_parts:
        asset_kind = "component"
    elif "services" in rel_parts:
        asset_kind = "service"
    elif "public" in rel_parts:
        asset_kind = "public"
    elif "webclient" in rel_parts:
        asset_kind = "webclient"
    else:
        asset_kind = file_path.suffix.lstrip(".")

    components = sorted({match.group(1) for match in COMPONENT_RE.finditer(text)})
    registry_entries = sorted({f"{match.group(2)}:{match.group(4)}" for match in REGISTRY_RE.finditer(text)})
    templates = sorted({match.group(2) for match in TEMPLATE_RE.finditer(text)})

    return FrontendAssetInfo(
        note_name=safe_filename(source_file),
        source_file=source_file,
        asset_kind=asset_kind,
        component_classes=components,
        registry_entries=registry_entries,
        templates=templates,
    )


def scan_frontend(module_dir: Path) -> List[FrontendAssetInfo]:
    static_src = module_dir / "static" / "src"
    if not static_src.exists():
        return []
    assets: List[FrontendAssetInfo] = []
    for file_path in sorted(static_src.rglob("*")):
        if not file_path.is_file() or file_path.suffix not in FRONTEND_EXTENSIONS:
            continue
        if any(part in {"tests", "test"} for part in file_path.parts):
            continue
        assets.append(parse_frontend_file(module_dir, file_path))
    return assets


def scan_addons(addons_root: Path) -> List[Path]:
    if not addons_root or not addons_root.exists():
        return []
    return sorted([path for path in addons_root.iterdir() if is_module_dir(path)], key=lambda path: path.name)


def puml_alias(name: str) -> str:
    return safe_filename(name).replace(".", "_")


def compute_output_path(scope: str, module_name: str, output_root: Path) -> Path:
    return output_root / DOCS_DIR / scope / module_name / f"{module_name}.md"


def module_folder_path(scope: str, module_name: str, output_root: Path) -> Path:
    return output_root / DOCS_DIR / scope / module_name


def section_index_path(scope: str, module_name: str, section: str, output_root: Path) -> Path:
    return module_folder_path(scope, module_name, output_root) / f"{section}.md"


def section_item_path(scope: str, module_name: str, section: str, note_name: str, output_root: Path) -> Path:
    return module_folder_path(scope, module_name, output_root) / section / f"{note_name}.md"


def link_target(scope: str, module_name: str) -> str:
    return f"{DOCS_DIR}/{scope}/{module_name}/{module_name}"


def detail_link(scope: str, module_name: str, section: str) -> str:
    return f"{DOCS_DIR}/{scope}/{module_name}/{section}"


def detail_item_link(scope: str, module_name: str, section: str, note_name: str) -> str:
    return f"{DOCS_DIR}/{scope}/{module_name}/{section}/{note_name}"


def write_generated_note(path: Path, marker: str, body_lines: List[str], overwrite: bool = False) -> None:
    ensure_dir(path)
    content = "\n".join([marker, *body_lines, marker, ""])
    if overwrite or not path.exists():
        path.write_text(content, encoding="utf-8")
        return

    existing = path.read_text(encoding="utf-8", errors="ignore")
    if marker in existing:
        prefix, _, remainder = existing.partition(marker)
        _, _, suffix = remainder.partition(marker)
        path.write_text(prefix + content + suffix, encoding="utf-8")
        return
    path.write_text(content, encoding="utf-8")


def load_diagram_style(output_root: Path) -> List[str]:
    style_path = output_root / TEMPLATES_DIR / "DiagramStyles.puml"
    if not style_path.exists():
        return []
    lines = style_path.read_text(encoding="utf-8-sig", errors="ignore").splitlines()
    if lines:
        lines[0] = lines[0].lstrip("\ufeff")
    return lines


def plantuml_block(output_root: Path, body_lines: List[str]) -> List[str]:
    return ["```plantuml", "@startuml", *load_diagram_style(output_root), *body_lines, "@enduml", "```"]


def summarize_names(values: Iterable[str], limit: int = 8) -> str:
    unique = sorted({value for value in values if value})
    if not unique:
        return "none"
    if len(unique) <= limit:
        return ", ".join(f"`{item}`" for item in unique)
    shown = ", ".join(f"`{item}`" for item in unique[:limit])
    return f"{shown}, and {len(unique) - limit} more"


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


def build_module_analysis(scope: str, module_dir: Path, metadata: Dict[str, Any]) -> ModuleAnalysis:
    return ModuleAnalysis(
        scope=scope,
        module_name=module_dir.name,
        module_dir=module_dir,
        metadata=metadata,
        models=scan_models(module_dir),
        xml=scan_xml(module_dir),
        controllers=scan_controllers(module_dir),
        frontend_assets=scan_frontend(module_dir),
    )


def write_module_note(
    analysis: ModuleAnalysis,
    output_root: Path,
    source_label: str,
    source_base: Optional[Path],
    dep_links: List[str],
    overwrite: bool = False,
) -> None:
    metadata = analysis.metadata
    name = metadata.get("name") or analysis.module_name
    summary = metadata.get("summary") or ""
    path = compute_output_path(analysis.scope, analysis.module_name, output_root)
    tags = ["odoo", "community" if analysis.scope == "Community Addons" else "enterprise", "module"]

    relative_source = None
    try:
        if source_base:
            relative_source = analysis.module_dir.resolve().relative_to(source_base.resolve()).as_posix()
    except Exception:
        relative_source = None

    detail_lines = []
    if analysis.models:
        detail_lines.append(f"- Models: [[{detail_link(analysis.scope, analysis.module_name, MODEL_SECTION)}|{MODEL_SECTION}]] ({len(analysis.models)})")
    if analysis.xml.files:
        detail_lines.append(f"- Views and XML: [[{detail_link(analysis.scope, analysis.module_name, VIEW_SECTION)}|{VIEW_SECTION}]] ({len(analysis.xml.files)} files)")
    if analysis.controllers:
        detail_lines.append(f"- Controllers: [[{detail_link(analysis.scope, analysis.module_name, CONTROLLER_SECTION)}|{CONTROLLER_SECTION}]] ({len(analysis.controllers)})")
    if analysis.frontend_assets:
        detail_lines.append(f"- Frontend: [[{detail_link(analysis.scope, analysis.module_name, FRONTEND_SECTION)}|{FRONTEND_SECTION}]] ({len(analysis.frontend_assets)} files)")

    module_map = [
        f'title {name} - Generated Coverage',
        'component "Module Overview" as overview',
        f'component "Models\\n{len(analysis.models)}" as models',
        f'component "Views / XML\\n{analysis.xml.view_count} views\\n{len(analysis.xml.files)} files" as views',
        f'component "Controllers\\n{sum(len(item.routes) for item in analysis.controllers)} routes" as controllers',
        f'component "Frontend\\n{len(analysis.frontend_assets)} files" as frontend',
        f'component "Security / Data\\n{analysis.xml.rule_count} rules\\n{analysis.xml.access_entries} ACL rows" as security',
        "overview --> models",
        "overview --> views",
        "overview --> controllers",
        "overview --> frontend",
        "overview --> security",
    ]

    lines: List[str] = [
        "---",
        f"tags: [{', '.join(tags)}]",
        "---",
        "",
        f"# {name}",
        "",
        f"- Scope: {analysis.scope}",
        f"- Source: {source_label}/{relative_source}" if relative_source else f"- Source: {source_label}",
        f"- Dependencies: {', '.join(dep_links) if dep_links else 'none'}",
    ]

    if summary:
        lines.extend(["", "## Summary", "", summary])

    lines.extend(
        [
            "",
            "## Generated coverage",
            "",
            f"- Models: {len(analysis.models)}",
            f"- XML files with UI/data artifacts: {len(analysis.xml.files)}",
            f"- Views: {analysis.xml.view_count}",
            f"- Actions: {analysis.xml.action_count}",
            f"- Menus: {analysis.xml.menu_count}",
            f"- Rules (ir.rule): {analysis.xml.rule_count}",
            f"- Access CSV entries: {analysis.xml.access_entries}",
            f"- Controller units: {len(analysis.controllers)}",
            f"- Frontend asset files: {len(analysis.frontend_assets)}",
            "",
            "## Module map",
            "",
            *plantuml_block(output_root, module_map),
        ]
    )

    if detail_lines:
        lines.extend(["", "## Detail notes", "", *detail_lines])

    if analysis.models:
        lines.extend(["", "## Key models", ""])
        for model_name in [item.model_name for item in analysis.models[:12]]:
            lines.append(f"- `{model_name}`")

    lines.extend(
        [
            "",
            "## Navigation",
            "",
            f"- [[../{analysis.scope}/{analysis.scope}|Back to scope]]",
            f"- [[../../{DOCS_NOTE}|Back to docs]]",
            "",
        ]
    )
    write_generated_note(path, "<!-- GENERATED:MODULE -->", lines, overwrite=overwrite)


def write_section_index(
    analysis: ModuleAnalysis,
    output_root: Path,
    section: str,
    items: List[tuple[str, str]],
    scope_tag: str,
    overwrite: bool = False,
) -> None:
    if not items:
        return
    path = section_index_path(analysis.scope, analysis.module_name, section, output_root)
    lines: List[str] = [
        "---",
        f"tags: [odoo, {scope_tag}, generated, index]",
        "---",
        "",
        f"# {analysis.module_name} {section}",
        "",
        f"- Module: [[{link_target(analysis.scope, analysis.module_name)}|{analysis.module_name}]]",
        f"- Scope: {analysis.scope}",
        f"- Generated items: {len(items)}",
        "",
        "## Items",
        "",
    ]
    for label, note_name in items:
        lines.append(f"- [[{detail_item_link(analysis.scope, analysis.module_name, section, note_name)}|{label}]]")
    lines.extend(["", "## Navigation", "", f"- **Parent:** [[{link_target(analysis.scope, analysis.module_name)}]]", ""])
    write_generated_note(path, f"<!-- GENERATED:{section.upper()} -->", lines, overwrite=overwrite)


def write_model_notes(analysis: ModuleAnalysis, output_root: Path, scope_tag: str, overwrite: bool = False) -> None:
    index_items: List[tuple[str, str]] = []
    for model in analysis.models:
        note_name = safe_filename(model.model_name)
        index_items.append((model.model_name, note_name))
        path = section_item_path(analysis.scope, analysis.module_name, MODEL_SECTION, note_name, output_root)

        relation_targets = sorted({relation.target for relation in model.relations.values() if relation.target})
        relation_diagram = [
            f'title {model.model_name} - Direct Relations',
            f'class "{model.model_name}" as {puml_alias(model.model_name)}',
        ]
        for target in relation_targets[:12]:
            relation_diagram.append(f'class "{target}" as {puml_alias(target)}')
        for relation in list(model.relations.values())[:18]:
            if not relation.target:
                continue
            arrow = "-->" if relation.kind == "many2one" else "--|>" if relation.kind == "one2many" else ".."
            relation_diagram.append(f"{puml_alias(model.model_name)} {arrow} {puml_alias(relation.target)} : {relation.field}")

        field_type_counts = Counter(field.field_type for field in model.fields.values())
        action_methods = sorted(name for name in model.methods if name.startswith("action"))
        compute_methods = sorted(name for name in model.methods if name.startswith("_compute"))
        onchange_methods = sorted(name for name, item in model.methods.items() if "onchange" in item.decorators or name.startswith("_onchange"))

        lines: List[str] = [
            "---",
            f"tags: [odoo, {scope_tag}, generated, model]",
            "---",
            "",
            f"# {model.model_name}",
            "",
            f"- Module: [[{link_target(analysis.scope, analysis.module_name)}|{analysis.module_name}]]",
            f"- Scope: {analysis.scope}",
            f"- Defined in module: {'yes' if model.defined_in_module else 'extension only'}",
            f"- Source files: {summarize_names(model.source_files, limit=6)}",
            f"- Python classes: {summarize_names(model.python_classes, limit=6)}",
        ]
        if model.description:
            lines.append(f"- Description: {model.description}")
        if model.inherits:
            lines.append(f"- Inherits: {summarize_names(model.inherits, limit=6)}")

        lines.extend(
            [
                "",
                "## Field footprint",
                "",
                f"- Detected fields: {len(model.fields)}",
                f"- Field types: {', '.join(f'`{field_type}` x {count}' for field_type, count in sorted(field_type_counts.items())) or 'none'}",
                f"- Relation fields: {len(model.relations)}",
            ]
        )

        if model.fields:
            lines.extend(["", "## Sample fields", ""])
            for field_info in list(sorted(model.fields.values(), key=lambda item: item.name))[:20]:
                extras = []
                if field_info.comodel_name:
                    extras.append(f"comodel `{field_info.comodel_name}`")
                if field_info.related:
                    extras.append(f"related `{field_info.related}`")
                if field_info.compute:
                    extras.append(f"compute `{field_info.compute}`")
                if field_info.store is not None:
                    extras.append(f"store `{field_info.store}`")
                suffix = f" ({', '.join(extras)})" if extras else ""
                lines.append(f"- `{field_info.name}`: `{field_info.field_type}`{suffix}")

        lines.extend(
            [
                "",
                "## Method hints",
                "",
                f"- Detected methods: {len(model.methods)}",
                f"- Action methods: {summarize_names(action_methods, limit=8)}",
                f"- Compute methods: {summarize_names(compute_methods, limit=8)}",
                f"- Onchange methods: {summarize_names(onchange_methods, limit=8)}",
            ]
        )

        if model.relations:
            lines.extend(["", "## Direct relation diagram", "", *plantuml_block(output_root, relation_diagram)])

        lines.extend(["", "## Navigation", "", f"- **Parent:** [[{detail_link(analysis.scope, analysis.module_name, MODEL_SECTION)}]]", ""])
        write_generated_note(path, "<!-- GENERATED:MODEL -->", lines, overwrite=overwrite)

    write_section_index(analysis, output_root, MODEL_SECTION, index_items, scope_tag, overwrite=overwrite)


def write_view_notes(analysis: ModuleAnalysis, output_root: Path, scope_tag: str, overwrite: bool = False) -> None:
    index_items: List[tuple[str, str]] = []
    for xml_file in analysis.xml.files:
        index_items.append((xml_file.source_file, xml_file.note_name))
        path = section_item_path(analysis.scope, analysis.module_name, VIEW_SECTION, xml_file.note_name, output_root)
        lines: List[str] = [
            "---",
            f"tags: [odoo, {scope_tag}, generated, views]",
            "---",
            "",
            f"# {xml_file.source_file}",
            "",
            f"- Module: [[{link_target(analysis.scope, analysis.module_name)}|{analysis.module_name}]]",
            f"- Scope: {analysis.scope}",
            f"- Source file: `{xml_file.source_file}`",
            f"- Views: {len(xml_file.views)}",
            f"- Actions: {len(xml_file.actions)}",
            f"- Menus: {len(xml_file.menus)}",
            f"- Rules: {len(xml_file.rules)}",
        ]

        if xml_file.views:
            lines.extend(["", "## View records", ""])
            for view in xml_file.views:
                lines.append(f"### `{view.xml_id}`")
                lines.append(f"- Name: {view.name or 'unnamed'}")
                lines.append(f"- Model: `{view.model_name}`" if view.model_name else "- Model: not declared")
                lines.append(f"- Type: `{view.view_type}`" if view.view_type else "- Type: inferred from arch")
                if view.inherit_id:
                    lines.append(f"- Inherits: `{view.inherit_id}`")
                if view.root_tag:
                    lines.append(f"- Root tag: `{view.root_tag}`")
                lines.append(f"- Field references: {len(view.field_names)}")
                if view.field_names:
                    lines.append(f"- Sample fields: {summarize_names(view.field_names, limit=10)}")
                if view.button_names:
                    lines.append(f"- Buttons: {summarize_names(view.button_names, limit=10)}")
                lines.append(f"- XPath or positional patches: {view.xpath_count}")
                lines.append("")

        if xml_file.actions:
            lines.extend(["## Actions", ""])
            for action in xml_file.actions[:20]:
                lines.append(f"- `{action.get('id')}`: `{action.get('type')}` {action.get('name') or ''}".rstrip())
            lines.append("")

        if xml_file.menus:
            lines.extend(["## Menus", ""])
            for menu in xml_file.menus[:20]:
                lines.append(f"- `{menu.get('id')}`: {menu.get('name') or 'unnamed'}")
            lines.append("")

        lines.extend(["## Navigation", "", f"- **Parent:** [[{detail_link(analysis.scope, analysis.module_name, VIEW_SECTION)}]]", ""])
        write_generated_note(path, "<!-- GENERATED:VIEWFILE -->", lines, overwrite=overwrite)

    write_section_index(analysis, output_root, VIEW_SECTION, index_items, scope_tag, overwrite=overwrite)


def write_controller_notes(analysis: ModuleAnalysis, output_root: Path, scope_tag: str, overwrite: bool = False) -> None:
    index_items: List[tuple[str, str]] = []
    for controller in analysis.controllers:
        index_items.append((controller.title, controller.note_name))
        path = section_item_path(analysis.scope, analysis.module_name, CONTROLLER_SECTION, controller.note_name, output_root)
        lines: List[str] = [
            "---",
            f"tags: [odoo, {scope_tag}, generated, controller]",
            "---",
            "",
            f"# {controller.title}",
            "",
            f"- Module: [[{link_target(analysis.scope, analysis.module_name)}|{analysis.module_name}]]",
            f"- Scope: {analysis.scope}",
            f"- Source file: `{controller.source_file}`",
            f"- Base classes: {summarize_names(controller.base_classes, limit=6)}",
            f"- Routes: {len(controller.routes)}",
            "",
            "## Routes",
            "",
        ]
        for route in controller.routes:
            lines.append(f"### `{route.method_name}`")
            lines.append(f"- Paths: {summarize_names(route.paths, limit=10)}")
            if route.route_type:
                lines.append(f"- Type: `{route.route_type}`")
            if route.auth:
                lines.append(f"- Auth: `{route.auth}`")
            if route.website is not None:
                lines.append(f"- Website route: `{route.website}`")
            if route.readonly:
                lines.append(f"- Readonly: `{route.readonly}`")
            lines.append("")
        lines.extend(["## Navigation", "", f"- **Parent:** [[{detail_link(analysis.scope, analysis.module_name, CONTROLLER_SECTION)}]]", ""])
        write_generated_note(path, "<!-- GENERATED:CONTROLLER -->", lines, overwrite=overwrite)

    write_section_index(analysis, output_root, CONTROLLER_SECTION, index_items, scope_tag, overwrite=overwrite)


def write_frontend_notes(analysis: ModuleAnalysis, output_root: Path, scope_tag: str, overwrite: bool = False) -> None:
    index_items: List[tuple[str, str]] = []
    for asset in analysis.frontend_assets:
        index_items.append((asset.source_file, asset.note_name))
        path = section_item_path(analysis.scope, analysis.module_name, FRONTEND_SECTION, asset.note_name, output_root)
        lines: List[str] = [
            "---",
            f"tags: [odoo, {scope_tag}, generated, frontend]",
            "---",
            "",
            f"# {asset.source_file}",
            "",
            f"- Module: [[{link_target(analysis.scope, analysis.module_name)}|{analysis.module_name}]]",
            f"- Scope: {analysis.scope}",
            f"- Asset kind: `{asset.asset_kind}`",
            f"- Source file: `{asset.source_file}`",
            "",
            "## Detected frontend signals",
            "",
            f"- Component classes: {summarize_names(asset.component_classes, limit=10)}",
            f"- Registry entries: {summarize_names(asset.registry_entries, limit=10)}",
            f"- Templates: {summarize_names(asset.templates, limit=10)}",
            "",
            "## Navigation",
            "",
            f"- **Parent:** [[{detail_link(analysis.scope, analysis.module_name, FRONTEND_SECTION)}]]",
            "",
        ]
        write_generated_note(path, "<!-- GENERATED:FRONTEND -->", lines, overwrite=overwrite)

    write_section_index(analysis, output_root, FRONTEND_SECTION, index_items, scope_tag, overwrite=overwrite)


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
    parser.add_argument("--modules", help="Comma-separated list of module technical names to refresh")
    parser.add_argument("--output", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--scan", action="store_true", help="Scan local sources and refresh addon notes")
    parser.add_argument("--overwrite", action="store_true", help="Replace generated note sections instead of merging them")
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

    allowed_modules = {item.strip() for item in (args.modules or "").split(",") if item.strip()}
    entries: List[ModuleAnalysis] = []
    for scope, addons_root in (("Community Addons", config.get("community")), ("Enterprise Addons", config.get("enterprise"))):
        if not addons_root:
            continue
        for module_dir in scan_addons(addons_root):
            if allowed_modules and module_dir.name not in allowed_modules:
                continue
            manifest_path = module_dir / "__manifest__.py"
            if not manifest_path.exists():
                manifest_path = module_dir / "__openerp__.py"
            metadata = parse_manifest(manifest_path) if manifest_path.exists() else {}
            entries.append(build_module_analysis(scope, module_dir, metadata))

    scope_lookup: Dict[str, Dict[str, str]] = {"Community Addons": {}, "Enterprise Addons": {}}
    for entry in entries:
        scope_lookup[entry.scope][entry.module_name] = entry.scope

    grouped: Dict[str, Dict[str, List[str]]] = {"Community Addons": {}, "Enterprise Addons": {}}
    for entry in entries:
        category = categorize_module(entry.module_name, entry.metadata)
        grouped[entry.scope].setdefault(category, []).append(entry.module_name)

    for entry in entries:
        scope_tag = "community" if entry.scope == "Community Addons" else "enterprise"
        source_label = "odoo" if entry.scope == "Community Addons" else "enterprise"
        source_base = config.get("odoo") if entry.scope == "Community Addons" else config.get("enterprise")
        dep_links: List[str] = []
        for dependency in entry.metadata.get("depends") or []:
            dependency_scope = scope_lookup["Community Addons"].get(dependency) or scope_lookup["Enterprise Addons"].get(dependency)
            if dependency_scope:
                dep_links.append(f"[[{link_target(dependency_scope, dependency)}|{dependency}]]")
            else:
                dep_links.append(f"{dependency} (not documented)")

        write_module_note(entry, output_root, source_label, source_base, dep_links, overwrite=args.overwrite)
        write_model_notes(entry, output_root, scope_tag, overwrite=args.overwrite)
        write_view_notes(entry, output_root, scope_tag, overwrite=args.overwrite)
        write_controller_notes(entry, output_root, scope_tag, overwrite=args.overwrite)
        write_frontend_notes(entry, output_root, scope_tag, overwrite=args.overwrite)

    if not allowed_modules:
        for scope, categories in grouped.items():
            for category, module_names in categories.items():
                write_category_note(output_root, scope, category, module_names)

    print("Generation finished.")


if __name__ == "__main__":
    main()
