<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_kanban_inherit_timesheet`
- Name: hr.employee.kanban.timesheet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_kanban_view_employees`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_employee_tree_inherit_timesheet`
- Name: hr.employee.list.timesheet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_employee_view_form_inherit_timesheet`
- Name: hr.employee.form.timesheet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_hourly_cost.view_employee_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_timesheet`
- Buttons: `action_open_versions`, `action_timesheet_from_employee`
- XPath or positional patches: 1

## Actions

- `unlink_employee_action`: `server` Delete
- `timesheet_action_view_from_employee_form`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
