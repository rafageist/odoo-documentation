---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_template_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_template_views.xml`
- Views: 2
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `hr_version_payroll_list_view`
- Name: hr.version.payroll.list
- Model: `hr.version`
- Type: inferred from arch
- Inherits: `hr.hr_version_list_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `payslips_count`
- XPath or positional patches: 1

### `hr_contract_template_view_form`
- Name: hr.contract.template.view.form.inherit.hr_payroll
- Model: `hr.version`
- Type: inferred from arch
- Inherits: `hr.hr_contract_template_form_view`
- Root tag: `page`
- Field references: 5
- Sample fields: `hourly_wage`, `payroll_properties`, `resource_calendar_id`, `schedule_pay`, `wage_type`
- Buttons: `action_configure_template_inputs`
- XPath or positional patches: 6

## Actions

- `action_new_salary_attachment`: `server` Create Salary Adjustment
- `action_hr_salary_attachment_new`: `act_window` Salary Adjustment
- `action_hr_payslip_new`: `act_window` Payslip

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

