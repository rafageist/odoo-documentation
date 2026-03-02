<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_template_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `views/planning_template_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `planning_slot_template_view_search`
- Name: planning.slot.template.search
- Model: `planning.slot.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `role_id`
- XPath or positional patches: 0

### `planning_slot_template_view_kanban`
- Name: planning.slot.template.view.kanban
- Model: `planning.slot.template`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `role_id`
- XPath or positional patches: 0

### `planning_slot_template_view_tree`
- Name: planning.slot.template.list
- Model: `planning.slot.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `role_id`, `sequence`
- XPath or positional patches: 0

### `planning_slot_template_view_form`
- Name: planning.slot.template.form
- Model: `planning.slot.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `active`, `duration_days`, `end_time`, `role_id`, `start_time`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

<!-- GENERATED:VIEWFILE -->
