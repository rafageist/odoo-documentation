---
tags: [odoo, enterprise, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Enterprise Addons/voip/voip|voip]]
- Scope: Enterprise Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.voip
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base_setup.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `module_voip`
- Buttons: `%(voip.action_voip_provider_view)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip/Views]]

