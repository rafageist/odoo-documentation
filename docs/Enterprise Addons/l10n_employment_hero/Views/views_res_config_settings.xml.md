<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings.xml

- Module: [[docs/Enterprise Addons/l10n_employment_hero/l10n_employment_hero|l10n_employment_hero]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.employment_hero
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account.res_config_settings_view_form`
- Root tag: `block`
- Field references: 7
- Sample fields: `country_code`, `employment_hero_api_key`, `employment_hero_base_url`, `employment_hero_enable`, `employment_hero_identifier`, `employment_hero_journal_id`, `employment_hero_lock_date`
- Buttons: `%(action_eh_payroll_fetch_payrun)d`
- XPath or positional patches: 1

## Actions

- `action_eh_payroll_fetch_payrun`: `server` Fetch Payruns

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_employment_hero/Views]]

<!-- GENERATED:VIEWFILE -->
