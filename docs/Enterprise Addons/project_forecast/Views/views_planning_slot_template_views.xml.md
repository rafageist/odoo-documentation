<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_template_views.xml

- Module: [[docs/Enterprise Addons/project_forecast/project_forecast|project_forecast]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_template_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `planning_slot_template_inherit_view_search`
- Name: planning.slot.template.view.search.inherit
- Model: `planning.slot.template`
- Type: inferred from arch
- Inherits: `planning.planning_slot_template_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 2

### `planning_slot_template_inherit_view_kanban`
- Name: planning.slot.template.view.kanban.inherit
- Model: `planning.slot.template`
- Type: inferred from arch
- Inherits: `planning.planning_slot_template_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `planning_slot_template_view_tree`
- Name: planning.slot.template.list
- Model: `planning.slot.template`
- Type: inferred from arch
- Inherits: `planning.planning_slot_template_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `planning_slot_template_view_form`
- Name: planning.slot.template.form
- Model: `planning.slot.template`
- Type: inferred from arch
- Inherits: `planning.planning_slot_template_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_forecast/Views]]

<!-- GENERATED:VIEWFILE -->
