---
tags: [odoo, enterprise, generated, views]
---

# views/hr_salary_rule_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_salary_rule_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_hr_rule_filter`
- Name: hr.salary.rule.select
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `amount_python_compute`, `category_id`, `name`, `struct_id`
- XPath or positional patches: 0

### `hr_salary_rule_form`
- Name: hr.salary.rule.form
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 37
- Sample fields: `amount_fix`, `amount_other_input_id`, `amount_percentage`, `amount_percentage_base`, `amount_python_compute`, `amount_select`, `appears_on_employee_cost_dashboard`, `appears_on_payslip`, `bold`, `category_id`, and 27 more
- XPath or positional patches: 0

### `hr_salary_rule_view_list_m2m`
- Name: hr.salary.rule.view.list.m2m
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_rule_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_id`, `struct_id`
- XPath or positional patches: 0

### `hr_salary_rule_list`
- Name: hr.salary.rule.list
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `category_id`, `code`, `country_id`, `name`, `partner_id`, `sequence`, `struct_id`
- XPath or positional patches: 0

### `hr_salary_rule_benefit_selector_list`
- Name: hr.salary.rule.selector.list
- Model: `hr.salary.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `input_default_value`, `input_description`, `input_section`, `name`
- XPath or positional patches: 0

## Actions

- `action_salary_rule_form`: `act_window` Salary Rules

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

