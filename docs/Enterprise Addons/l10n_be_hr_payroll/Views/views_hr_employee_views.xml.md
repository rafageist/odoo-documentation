---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_form`
- Name: hr.employee.view.form
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `xpath`
- Field references: 82
- Sample fields: `car_atn`, `children`, `commission_on_target`, `currency_id`, `disabled_children_bool`, `disabled_children_number`, `disabled_spouse_bool`, `distance_home_work`, `distance_home_work_unit`, `double_pay_line_ids`, and 72 more
- Buttons: `action_open_attest_wizard`
- XPath or positional patches: 8

## Actions

- `action_employee_working_schedule_change_request`: `server` Working Schedule Change

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

