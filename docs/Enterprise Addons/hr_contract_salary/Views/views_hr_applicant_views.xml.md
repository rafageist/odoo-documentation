---
tags: [odoo, enterprise, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 1
- Actions: 0
- Menus: 2
- Rules: 0

## View records

### `hr_applicant_view_form`
- Name: hr.applicant.form
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `proposed_contracts_count`, `salary_offers_count`
- Buttons: `action_generate_offer`, `action_show_offers`, `action_show_proposed_contracts`, `create_employee_from_applicant`
- XPath or positional patches: 1

## Menus

- `hr_recruitment_menu_contract_templates`: Templates
- `menu_hr_recruitment_config_contract_templates`: Contracts

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

