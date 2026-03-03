---
tags: [odoo, enterprise, generated, views]
---

# views/hr_salary_rule_category_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_salary_rule_category_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_hr_salary_rule_category_filter`
- Name: hr.salary.rule.category.select
- Model: `hr.salary.rule.category`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_salary_rule_category_tree`
- Name: hr.salary.rule.category.list
- Model: `hr.salary.rule.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `code`, `country_id`, `name`, `parent_id`
- XPath or positional patches: 0

### `hr_salary_rule_category_form`
- Name: hr.salary.rule.category.form
- Model: `hr.salary.rule.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `code`, `country_id`, `name`, `note`, `parent_id`
- XPath or positional patches: 0

## Actions

- `action_hr_salary_rule_category`: `act_window` Salary Rule Categories

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

