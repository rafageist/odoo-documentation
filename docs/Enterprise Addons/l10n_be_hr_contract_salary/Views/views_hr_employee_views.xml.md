<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_contract_salary/l10n_be_hr_contract_salary|l10n_be_hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_form`
- Name: hr.employee.view.form
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `holidays`
- XPath or positional patches: 1

### `l10n_be_hr_contract_salary_view_employee_form`
- Name: hr.employee.form.inherit.l10n_be.contract_salary
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `label`
- Field references: 1
- Sample fields: `l10n_be_wage_with_mobility_budget`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_contract_salary/Views]]

<!-- GENERATED:VIEWFILE -->
