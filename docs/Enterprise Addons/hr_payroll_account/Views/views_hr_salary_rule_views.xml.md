<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_salary_rule_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/hr_salary_rule_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_salary_rule_list`
- Name: hr.salary.rule.list.inherit
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_rule_list`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `account_credit`, `account_debit`, `credit_tag_ids`, `debit_tag_ids`
- XPath or positional patches: 1

### `hr_salary_rule_view_form`
- Name: hr.salary.rule.form.inherit
- Model: `hr.salary.rule`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_salary_rule_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `account_credit`, `account_debit`, `analytic_distribution`, `credit_tag_ids`, `debit_tag_ids`, `employee_move_line`, `not_computed_in_net`, `split_move_lines`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
