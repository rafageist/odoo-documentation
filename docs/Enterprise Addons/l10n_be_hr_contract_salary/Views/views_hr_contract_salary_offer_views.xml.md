---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_offer_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_contract_salary/l10n_be_hr_contract_salary|l10n_be_hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_offer_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_contract_salary_offer_view_search`
- Name: hr.contract.salary.offer.view.search.inherit
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_offer_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `hr_contract_salary_offer_view_tree`
- Name: hr.contract.salary.offer.view.list.inherit
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_offer_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `car_id`, `contract_template_id`
- XPath or positional patches: 0

### `hr_contract_salary_offer_view_form`
- Name: hr.contract.salary.offer.view.form.inherit
- Model: `hr.contract.salary.offer`
- Type: inferred from arch
- Inherits: `hr_contract_salary.hr_contract_salary_offer_view_form`
- Root tag: `field`
- Field references: 9
- Sample fields: `additional_car_ids`, `assigned_car_warning`, `car_id`, `contract_type_id`, `country_code`, `job_title`, `l10n_be_canteen_cost`, `new_car`, `wishlist_car_warning`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_contract_salary/Views]]

