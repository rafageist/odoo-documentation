<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/account_update_tax_tags/account_update_tax_tags|account_update_tax_tags]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.account_update_tax_tags
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `account.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(account_update_tax_tags.action_open_wizard)d`
- XPath or positional patches: 1

## Actions

- `action_open_wizard`: `act_window` Update tax tags on existing Journal Entries

## Navigation

- **Parent:** [[docs/Community Addons/account_update_tax_tags/Views]]

<!-- GENERATED:VIEWFILE -->
