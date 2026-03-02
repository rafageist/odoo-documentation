<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `payroll_hr_employee_view_search`
- Name: hr.employee.search.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `registration_number`
- XPath or positional patches: 7

### `payroll_hr_employee_view_kanban`
- Name: payroll.hr.employee.view.kanban.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_kanban_view_employees`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `payroll_hr_employee_view_tree_employee_trends`
- Name: payroll.hr.employee.view.list.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `registration_number`
- XPath or positional patches: 1

### `payroll_hr_employee_view_form`
- Name: payroll.hr.employee.view.form
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 15
- Sample fields: `disabled`, `hourly_wage`, `internet_invoice`, `is_non_resident`, `lang`, `marital`, `payroll_properties`, `payslip_count`, `registration_number`, `resource_calendar_id`, and 5 more
- Buttons: `%(action_hr_payslip_new)d`, `action_configure_employee_inputs`, `action_open_payslips`, `action_open_versions`
- XPath or positional patches: 10

## Actions

- `action_index_employee_contracts_list`: `server` Index contract(s)
- `action_index_employee_contracts_form`: `server` Index contract(s)

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
