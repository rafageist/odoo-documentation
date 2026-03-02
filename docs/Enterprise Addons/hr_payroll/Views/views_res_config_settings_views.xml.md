<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.payroll
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `hr.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `contract_expiration_notice_period`, `module_hr_payroll_account_iso20022`, `module_l10n_be_hr_payroll`, `module_l10n_fr_hr_payroll`, `module_l10n_in_hr_payroll`, `work_permit_expiration_notice_period`, `ytd_reset_day`, `ytd_reset_month`
- Buttons: `%(open_payroll_modules)d`
- XPath or positional patches: 1

## Actions

- `action_hr_payroll_configuration`: `act_window` Settings
- `open_payroll_modules`: `act_window` Payroll

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
