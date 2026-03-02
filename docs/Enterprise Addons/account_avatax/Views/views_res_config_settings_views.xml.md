<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/account_avatax/account_avatax|account_avatax]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.account.avatax
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account.res_config_settings_view_form`
- Root tag: `setting`
- Field references: 8
- Sample fields: `avalara_address_validation`, `avalara_api_id`, `avalara_api_key`, `avalara_commit`, `avalara_environment`, `avalara_partner_code`, `avalara_use_upc`, `setting_account_avatax`
- Buttons: `account_avatax.ir_logging_avalara_action`, `avatax_log`, `avatax_ping`, `avatax_sync_company_params`
- XPath or positional patches: 1

### `ir_logging_avalara_tree`
- Name: ir.logging.avalara
- Model: `ir.logging`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `func`, `line`, `message`, `path`
- XPath or positional patches: 0

## Actions

- `ir_logging_avalara_action`: `act_window` Avalara Logging

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_avatax/Views]]

<!-- GENERATED:VIEWFILE -->
