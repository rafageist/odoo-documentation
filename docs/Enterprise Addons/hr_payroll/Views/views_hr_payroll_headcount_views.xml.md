---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_headcount_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_headcount_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_payroll_headcount_line_search`
- Name: hr.payroll.headcount.line.search
- Model: `hr.payroll.headcount.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `job_id`
- XPath or positional patches: 0

### `hr_payroll_headcount_line_view_tree`
- Name: hr.payroll.headcount.line.view.list
- Model: `hr.payroll.headcount.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `currency_id`, `department_id`, `employee_id`, `employee_type`, `job_id`, `version_names`, `wage_on_payroll`, `working_rate_ids`
- XPath or positional patches: 0

### `hr_payroll_headcount_view_search`
- Name: hr.payroll.headcount.view.search
- Model: `hr.payroll.headcount`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `create_uid`, `employee_count`, `name`, `write_date`
- XPath or positional patches: 0

### `hr_payroll_headcount_view_tree`
- Name: hr.payroll.headcount.view.list
- Model: `hr.payroll.headcount`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `create_uid`, `employee_count`, `name`, `write_date`
- XPath or positional patches: 0

### `hr_payroll_headcount_view_form`
- Name: hr.payroll.headcount.view.form
- Model: `hr.payroll.headcount`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `date_from`, `date_to`, `display_name`, `employee_count`, `name`
- Buttons: `action_open_lines`, `action_populate`
- XPath or positional patches: 0

## Actions

- `hr_payroll_headcount_action`: `act_window` Headcount

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

