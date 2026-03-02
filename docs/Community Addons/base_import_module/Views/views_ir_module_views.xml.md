<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/ir_module_views.xml

- Module: [[docs/Community Addons/base_import_module/base_import_module|base_import_module]]
- Scope: Community Addons
- Source file: `views/ir_module_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_module_filter_apps_inherit`
- Name: Search Data Modules
- Model: `ir.module.module`
- Type: inferred from arch
- Inherits: `base.view_module_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `module_type`
- XPath or positional patches: 1

### `module_form_apps_inherit`
- Name: Apps
- Model: `ir.module.module`
- Type: inferred from arch
- Inherits: `base.module_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `button_immediate_install_app`
- XPath or positional patches: 4

### `module_tree_apps_inherit`
- Name: Apps List Data Modules
- Model: `ir.module.module`
- Type: inferred from arch
- Inherits: `base.module_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `installed_version`, `module_type`, `name`
- XPath or positional patches: 1

### `module_view_kanban_apps_inherit`
- Name: Apps Kanban Data Modules
- Model: `ir.module.module`
- Type: inferred from arch
- Inherits: `base.module_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `module_type`
- Buttons: `button_immediate_install_app`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/base_import_module/Views]]

<!-- GENERATED:VIEWFILE -->
