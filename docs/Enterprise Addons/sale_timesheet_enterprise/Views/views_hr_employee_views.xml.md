---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_timesheet_employee_list_inherit`
- Name: sale.timesheet.employee.list.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_employee_list_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `billable_time_target`, `timesheet_manager_id`
- XPath or positional patches: 3

### `view_employee_form`
- Name: view.employee.form.inherit.hr.employee.billable.time.target
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `group`
- Field references: 2
- Sample fields: `billable_time_target`, `show_billable_time_target`
- XPath or positional patches: 1

## Actions

- `action_open_view_employee`: `act_window` Employees

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_timesheet_enterprise/Views]]

