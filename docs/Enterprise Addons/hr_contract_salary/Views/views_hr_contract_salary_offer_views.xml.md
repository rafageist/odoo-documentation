<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_offer_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_offer_views.xml`
- Views: 3
- Actions: 6
- Menus: 2
- Rules: 0

## View records

### `hr_contract_salary_offer_view_search`
- Name: hr.contract.salary.offer.view.search
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `applicant_name`, `display_name`, `employee_id`
- XPath or positional patches: 0

### `hr_contract_salary_offer_view_form`
- Name: hr.contract.salary.offer.view.form
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `access_token`, `applicant_id`, `company_id`, `contract_end_date`, `contract_start_date`, `contract_template_id`, `create_date`, `currency_id`, `department_id`, `display_name`, and 11 more
- Buttons: `action_edit_offer_signatories`, `action_jump_to_offer`, `action_send_by_email`, `action_view_signature_request`, `action_view_version`
- XPath or positional patches: 0

### `hr_contract_salary_offer_view_tree`
- Name: hr.contract.salary.offer.view.list
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `applicant_id`, `company_id`, `contract_start_date`, `contract_template_id`, `create_date`, `create_uid`, `currency_id`, `department_id`, `display_name`, `employee_id`, and 5 more
- XPath or positional patches: 0

## Actions

- `action_view_partially_signed_contract_statbutton`: `act_window` Contract Details (Read Only)
- `action_view_contract_statbutton`: `act_window` Contract Details
- `hr_contract_salary_offer_recruitment_action`: `act_window` Offers
- `action_refuse_salary_offer`: `server` Refuse
- `hr_contract_salary_offer_action`: `act_window` Offers
- `action_hr_offer_new`: `act_window` Offer

## Menus

- `menu_hr_contract_salary_job_offer`: unnamed
- `menu_salary_package_offer`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

<!-- GENERATED:VIEWFILE -->
