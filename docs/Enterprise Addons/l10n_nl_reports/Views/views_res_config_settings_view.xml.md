---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_view.xml

- Module: [[docs/Enterprise Addons/l10n_nl_reports/l10n_nl_reports|l10n_nl_reports]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.l10n.nl.reports
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account_reports.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_nl_rounding_difference_loss_account_id`, `l10n_nl_rounding_difference_profit_account_id`
- XPath or positional patches: 1

### `res_config_settings_view_form_l10n_nl`
- Name: res.config.settings.view.form
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `l10n_nl.res_config_settings_view_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `l10n_nl_reports_sbr_cert_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_nl_reports/Views]]

