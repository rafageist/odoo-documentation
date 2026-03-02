<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.l10n_au_hr_payroll_account
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `l10n_au_bms_id`, `l10n_au_hr_super_responsible_id`, `l10n_au_previous_bms_id`, `l10n_au_stp_responsible_id`, `l10n_au_superstream_payable_account_id`
- Buttons: `%(l10n_au_hr_payroll_account.action_open_transfer_previous_payroll)d`
- XPath or positional patches: 1

## Actions

- `action_open_transfer_previous_payroll`: `act_window` Import YTD Balances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Views]]

<!-- GENERATED:VIEWFILE -->
