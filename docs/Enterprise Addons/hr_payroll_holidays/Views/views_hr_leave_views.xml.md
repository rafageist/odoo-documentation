<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_leave_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
- Scope: Enterprise Addons
- Source file: `views/hr_leave_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `hr_leave_view_tree_inherit_payroll`
- Name: hr.holidays.view.list.inherit.work.entry
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `payslip_state`
- XPath or positional patches: 1

### `hr_leave_view_form_inherit`
- Name: hr.leave.view.form.inherit
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_form_manager`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `payslip_state`
- Buttons: `action_back_to_approval`, `action_report_to_next_month`
- XPath or positional patches: 1

### `hr_leave_view_search`
- Name: hr.leave.view.form.inherit.hr.payroll.holidays
- Model: `hr.leave`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_view_search_manager`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_registration_number`
- XPath or positional patches: 2

## Actions

- `hr_leave_work_entry_action`: `act_window` Time Off
- `hr_leave_action_open_to_defer`: `act_window` Time Off to Defer

## Menus

- `menu_work_entry_leave_to_approve`: Time Offs

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
