---
tags: [odoo, enterprise, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Enterprise Addons/voip/voip|voip]]
- Scope: Enterprise Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_users_view_form_preferences`
- Name: VoIP Config in Preferences Form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `external_device_number`, `how_to_call_on_mobile`, `should_call_from_another_device`, `voip_provider_id`, `voip_secret`, `voip_username`
- Buttons: `%(voip.action_voip_provider_view)d`
- XPath or positional patches: 1

### `res_user_form`
- Name: VoIP Config in User Form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `external_device_number`, `how_to_call_on_mobile`, `should_call_from_another_device`, `voip_provider_id`, `voip_secret`, `voip_username`
- Buttons: `%(voip.action_voip_provider_view)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip/Views]]

