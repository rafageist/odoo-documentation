<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/auth_passkey/auth_passkey|auth_passkey]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `auth_passkey_users_preferences`
- Name: auth.passkey.users.preferences
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `auth_passkey_key_ids`
- Buttons: `action_create_passkey`
- XPath or positional patches: 1

### `auth_passkey_users_form`
- Name: auth.passkey.users.form
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `auth_passkey_key_ids`
- Buttons: `action_create_passkey`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/auth_passkey/Views]]

<!-- GENERATED:VIEWFILE -->
