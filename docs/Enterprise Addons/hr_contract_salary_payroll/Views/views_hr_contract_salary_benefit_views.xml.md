<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_benefit_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_benefit_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_contract_benefit_view_form`
- Name: hr.contract.salary.benefit.view.form.inherit.hr_contract_salary_payroll
- Model: `hr.contract.salary.benefit`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_benefit_view_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `benefit_type_id`, `salary_rule_id`, `source`
- XPath or positional patches: 0

### `hr_contract_benefit_view_tree`
- Name: hr.contract.salary.benefit.view.list.inherit.hr_contract_salary_payroll
- Model: `hr.contract.salary.benefit`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_benefit_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `res_field_id`, `salary_rule_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
