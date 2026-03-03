---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_line_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_line_views.xml`
- Views: 8
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_line_view_search_report`
- Name: hr.payslip.line.search.report
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `employee_id`, `name`, `slip_id`
- XPath or positional patches: 0

### `hr_payslip_line_view_list_report`
- Name: hr.payslip.line.list.report
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `amount`, `category_id`, `code`, `company_id`, `employee_id`, `name`, `quantity`, `rate`, `sequence`, `total`
- XPath or positional patches: 0

### `hr_payslip_line_view_pivot`
- Name: hr.payslip.line.pivot
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount`, `date_from`, `salary_rule_id`
- XPath or positional patches: 0

### `hr_payslip_line_view_search_register`
- Name: hr.payslip.line.search.view
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `amount_select`, `date_from`, `name`, `partner_id`, `slip_id`
- XPath or positional patches: 0

### `view_hr_payslip_line_filter`
- Name: hr.payslip.line.select
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `amount_select`, `name`, `slip_id`
- XPath or positional patches: 0

### `view_hr_payslip_line_form`
- Name: hr.payslip.line.form
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `amount_fix`, `amount_percentage`, `amount_select`, `category_id`, `code`, `employee_id`, `name`, `partner_id`, `sequence`, `slip_id`
- XPath or positional patches: 0

### `view_hr_payslip_line_tree_register`
- Name: hr.payslip.line.list.register
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount_select`, `code`, `employee_id`, `partner_id`, `slip_id`, `total`
- XPath or positional patches: 0

### `view_hr_payslip_line_tree`
- Name: hr.payslip.line.list
- Model: `hr.payslip.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `amount`, `amount_select`, `category_id`, `code`, `company_id`, `employee_id`, `name`, `partner_id`, `quantity`, `rate`, and 2 more
- XPath or positional patches: 0

## Actions

- `hr_payslip_line_action_report_view_list`: `view`
- `hr_payslip_line_action_report_view_pivot`: `view`
- `hr_payslip_line_action_report`: `act_window` Payslip Lines Report
- `act_contribution_reg_payslip_lines`: `act_window` Payslip Lines
- `action_contribution_registers_view_form`: `view`
- `action_contribution_registers_view_list`: `view`
- `action_contribution_registers`: `act_window` Contribution Registers

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

