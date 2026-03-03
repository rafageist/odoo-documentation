---
tags: [odoo, enterprise, generated, views]
---

# views/hr_contract_salary_benefit_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/hr_contract_salary_benefit_views.xml`
- Views: 3
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `hr_contract_benefit_view_form`
- Name: hr.contract.salary.benefit.view.form
- Model: `hr.contract.salary.benefit`
- Type: inferred from arch
- Root tag: `form`
- Field references: 35
- Sample fields: `activity_creation`, `activity_creation_type`, `activity_responsible_id`, `activity_type_id`, `always_show_description`, `benefit_ids`, `benefit_type_id`, `cost_res_field_id`, `cost_res_field_public`, `description`, and 25 more
- XPath or positional patches: 0

### `hr_contract_benefit_view_search`
- Name: hr.contract.salary.benefit.view.search
- Model: `hr.contract.salary.benefit`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_contract_benefit_view_tree`
- Name: hr.contract.salary.benefit.view.list
- Model: `hr.contract.salary.benefit`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `field`, `name`, `res_field_id`, `sequence`, `source`, `structure_type_id`
- XPath or positional patches: 0

## Actions

- `hr_contract_benefit_action`: `act_window` Benefits

## Menus

- `salary_package_benefit`: unnamed
- `salary_package_menu`: Salary Package Configurator

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

