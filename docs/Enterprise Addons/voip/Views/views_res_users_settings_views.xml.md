<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_users_settings_views.xml

- Module: [[docs/Enterprise Addons/voip/voip|voip]]
- Scope: Enterprise Addons
- Source file: `views/res_users_settings_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `voip_res_users_settings_view_form`
- Name: VoIP User Settings
- Model: `res.users.settings`
- Type: inferred from arch
- Inherits: `mail.res_users_settings_view_form`
- Root tag: `group`
- Field references: 5
- Sample fields: `external_device_number`, `how_to_call_on_mobile`, `should_call_from_another_device`, `voip_secret`, `voip_username`
- Buttons: `%(voip_call_action_history)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip/Views]]

<!-- GENERATED:VIEWFILE -->
