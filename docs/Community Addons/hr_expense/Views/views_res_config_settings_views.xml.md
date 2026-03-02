<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.expense
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `company_expense_allowed_payment_method_line_ids`, `expense_journal_id`, `hr_expense_alias_domain_id`, `hr_expense_alias_prefix`, `hr_expense_use_mailgateway`, `module_hr_expense_extract`, `module_hr_expense_stripe`, `module_hr_payroll_expense`
- XPath or positional patches: 1

## Actions

- `action_hr_expense_configuration`: `act_window` Settings

## Menus

- `menu_hr_expense_global_settings`: Settings

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Views]]

<!-- GENERATED:VIEWFILE -->
