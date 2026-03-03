---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_hr`
- Name: res.config.settings.view.form.inherit.hr.contract.salary
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_salary_simulator_link_validity`
- XPath or positional patches: 1

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.contract.salary
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr_recruitment.res_config_settings_view_form`
- Root tag: `block`
- Field references: 1
- Sample fields: `access_token_validity`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_contract_salary/Views]]

