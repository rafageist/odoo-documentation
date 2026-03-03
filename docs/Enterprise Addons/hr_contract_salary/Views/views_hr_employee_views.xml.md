---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_contract_salary_view_employee_form_readonly`
- Name: hr.employee.form.inherit.contract_salary.readonly
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `hr_contract_salary_view_employee_form`
- Name: hr.employee.form.inherit.contract_salary
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `contract_reviews_count`, `current_date_version`, `final_yearly_costs`, `monthly_yearly_costs`, `originated_offer_id`, `salary_offers_count`, `wage_on_signature`, `wage_with_holidays`
- Buttons: `action_generate_offer`, `action_open_versions`, `action_show_contract_reviews`, `action_show_offers`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

