---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_worked_days_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_worked_days_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_payslip_work_days_view_search_report`
- Name: hr.payslip.worked_days.search.report
- Model: `hr.payslip.worked_days`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `employee_id`, `name`, `payslip_id`
- XPath or positional patches: 0

### `hr_payslip_work_days_view_pivot`
- Name: hr.payslip.worked_days.pivot
- Model: `hr.payslip.worked_days`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount`, `date_from`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_payslip_work_days_view_list`
- Name: hr.payslip.worked_days.list
- Model: `hr.payslip.worked_days`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount`, `employee_id`, `name`, `number_of_days`, `number_of_hours`, `payslip_id`
- XPath or positional patches: 0

## Actions

- `hr_payslip_work_days_action_report_view_pivot`: `view`
- `hr_payslip_work_days_action_report`: `act_window` Payslip Work Days Lines Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

