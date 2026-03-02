<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_resume_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary_payroll/hr_contract_salary_payroll|hr_contract_salary_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_resume_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_contract_salary_resume_view_search_inherit`
- Name: view.resource.calendar.search.inherit.payroll
- Model: `hr.contract.salary.resume`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_resume_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_contract_salary_resume_view_form`
- Name: hr.contract.salary.resume.view.form.inherit.hr.contract.salary.payroll
- Model: `hr.contract.salary.resume`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_resume_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `hr_contract_salary.hr_contract_salary_resume_action`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
