---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee.xml

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_search_view`
- Name: hr.employee.search.view
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `timesheet_manager_id`
- XPath or positional patches: 2

### `view_employee_tree_inherit_timesheet`
- Name: hr.employee.list.timesheet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `timesheet_manager_id`
- XPath or positional patches: 1

### `hr_employee_view_form_inherit_timesheet_validation`
- Name: hr.employee.form.timesheet.validation
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_employee_view_form_inherit_timesheet`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `timesheet_manager_id`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Views]]

