---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings.xml

- Module: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.expense.stripe
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr_expense.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `module_hr_expense_stripe`, `stripe_account_issuing_status`, `stripe_account_issuing_tos_accepted`, `stripe_journal_id`
- Buttons: `action_configure_stripe_account`, `action_create_stripe_account`, `action_refresh_stripe_account`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe/Views]]

