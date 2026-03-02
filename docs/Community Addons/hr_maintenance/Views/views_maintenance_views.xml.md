<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/maintenance_views.xml

- Module: [[docs/Community Addons/hr_maintenance/hr_maintenance|hr_maintenance]]
- Scope: Community Addons
- Source file: `views/maintenance_views.xml`
- Views: 8
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `maintenance_equipment_view_tree_inherit_hr`
- Name: maintenance.equipment.view.list.inherit.hr
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `department_id`, `employee_id`
- XPath or positional patches: 1

### `maintenance_equipment_view_kanban_inherit_hr`
- Name: maintenance.equipment.view.kanban.inherit.hr
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `department_id`, `employee_id`
- XPath or positional patches: 2

### `maintenance_equipment_view_form_inherit_hr`
- Name: maintenance.equipment.view.form.inherit.hr
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `equipment_assign_to`
- XPath or positional patches: 1

### `maintenance_equipment_view_search_inherit_hr`
- Name: maintenance.equipment.view.search.inherit.hr
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_view_search`
- Root tag: `filter`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `owner_user_id`
- XPath or positional patches: 3

### `maintenance_request_view_tree_inherit_hr`
- Name: maintenance.request.view.list.inherit.hr
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

### `maintenance_request_view_kanban_inherit_hr`
- Name: maintenance.request.view.kanban.inherit.hr
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

### `maintenance_request_view_form_inherit_hr`
- Name: maintenance.request.view.form.inherit.hr
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

### `maintenance_request_view_search_inherit_hr`
- Name: maintenance.request.view.search.inherit.hr
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/hr_maintenance/Views]]

<!-- GENERATED:VIEWFILE -->
