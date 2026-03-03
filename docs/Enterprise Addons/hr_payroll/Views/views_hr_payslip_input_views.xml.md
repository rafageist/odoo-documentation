---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_input_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_input_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_input_view_list`
- Name: hr.payslip.input.list
- Model: `hr.payslip.input`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `amount`, `employee_id`, `input_type_id`, `payslip_id`
- XPath or positional patches: 0

### `hr_payslip_input_view_pivot`
- Name: hr.payslip.input.pivot
- Model: `hr.payslip.input`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `amount`, `date_from`
- XPath or positional patches: 0

### `hr_payslip_input_view_search_report`
- Name: hr.payslip.input.search.report
- Model: `hr.payslip.input`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `employee_id`, `name`, `payslip_id`
- XPath or positional patches: 0

## Actions

- `hr_payslip_input_action_report`: `act_window` Payslip Other Inputs Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

