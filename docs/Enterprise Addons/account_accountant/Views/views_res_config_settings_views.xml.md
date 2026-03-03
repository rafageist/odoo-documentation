---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.account.accountant
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 16
- Sample fields: `deferred_expense_account_id`, `deferred_expense_amount_computation_method`, `deferred_expense_journal_id`, `deferred_revenue_account_id`, `deferred_revenue_amount_computation_method`, `deferred_revenue_journal_id`, `fiscalyear_last_day`, `fiscalyear_last_month`, `generate_deferred_expense_entries_method`, `generate_deferred_revenue_entries_method`, and 6 more
- Buttons: `%(account_accountant.actions_account_fiscal_year)d`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Views]]

