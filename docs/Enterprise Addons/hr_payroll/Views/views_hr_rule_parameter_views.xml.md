<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_rule_parameter_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_rule_parameter_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_rule_parameter_view_search`
- Name: hr.rule.parameter.search
- Model: `hr.rule.parameter`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_rule_parameter_view_tree`
- Name: hr.rule.parameter.list
- Model: `hr.rule.parameter`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `code`, `current_value_one_line`, `name`, `salary_rule_ids`, `valid_since`
- Buttons: `action_open_salary_rules`
- XPath or positional patches: 0

### `hr_rule_parameter_view_form`
- Name: hr.rule.parameter.form
- Model: `hr.rule.parameter`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `code`, `date_from`, `description`, `name`, `parameter_value`, `parameter_version_ids`, `salary_rule_count`
- Buttons: `action_open_salary_rules`
- XPath or positional patches: 0

## Actions

- `hr_rule_parameter_action`: `act_window` Salary Rule Parameters

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
