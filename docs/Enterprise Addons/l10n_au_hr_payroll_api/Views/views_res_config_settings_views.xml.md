---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.l10n_au_hr_payroll_account
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `l10n_au_hr_payroll_account.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `l10n_au_bms_id`, `l10n_au_hr_super_responsible_id`, `l10n_au_payroll_mode`, `l10n_au_registration_status`, `l10n_au_stp_responsible_id`
- Buttons: `action_view_payroll_onboarding`, `cancel_ongoing_registration`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Views]]

