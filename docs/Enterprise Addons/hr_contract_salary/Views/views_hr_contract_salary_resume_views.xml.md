---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_resume_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_resume_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_contract_salary_resume_view_form`
- Name: hr.contract.salary.resume.view.form
- Model: `hr.contract.salary.resume`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `benefit_ids`, `category_id`, `code`, `fixed_value`, `impacts_monthly_total`, `name`, `structure_type_id`, `uom`, `value_type`
- XPath or positional patches: 0

### `hr_contract_salary_resume_view_tree`
- Name: hr.contract.salary.resume.view.list
- Model: `hr.contract.salary.resume`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `code`, `name`, `sequence`, `structure_type_id`, `value_type`
- XPath or positional patches: 0

### `hr_contract_salary_resume_view_search`
- Name: hr.contract.salary.resume.view.search
- Model: `hr.contract.salary.resume`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `structure_type_id`, `value_type`
- XPath or positional patches: 0

## Actions

- `hr_contract_salary_resume_action`: `act_window` Resume

## Menus

- `salary_package_resume`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

