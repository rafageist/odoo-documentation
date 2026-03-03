---
tags: [odoo, enterprise, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Enterprise Addons/voip_onsip/voip_onsip|voip_onsip]]
- Scope: Enterprise Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `onsip_res_users_view_form_preferences`
- Name: VOIP OnSIP in Preferences Form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `onsip_auth_username`
- XPath or positional patches: 1

### `onsip_res_user_form`
- Name: VOIP OnSIP in User Form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `voip.res_user_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `onsip_auth_username`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip_onsip/Views]]

