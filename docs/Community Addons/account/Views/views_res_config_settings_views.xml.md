<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form_base_setup`
- Name: res.config.settings.view.form.inherit.base_setup
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base_setup.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.account
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 60
- Sample fields: `account_cash_basis_base_account_id`, `account_default_credit_limit`, `account_discount_expense_allocation_id`, `account_discount_income_allocation_id`, `account_fiscal_country_id`, `account_journal_early_pay_discount_gain_account_id`, `account_journal_early_pay_discount_loss_account_id`, `account_journal_suspense_account_id`, `account_price_include`, `account_storno`, and 50 more
- Buttons: `%(account.rounding_list_action)d`, `%(base.action_currency_form)d`, `%(uom.product_uom_form_action)d`, `action_eu_oss_tax_mapping`, `action_update_terms`, `reload_template`
- XPath or positional patches: 1

## Actions

- `action_account_config`: `act_window` Settings
- `open_account_charts_modules`: `act_window` Chart Templates

## Navigation

- **Parent:** [[docs/Community Addons/account/Views]]

<!-- GENERATED:VIEWFILE -->
