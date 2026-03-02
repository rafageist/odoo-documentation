<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/auth_totp/auth_totp|auth_totp]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_totp_field`
- Name: users preference: totp
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `totp_enabled`
- Buttons: `action_totp_disable`, `action_totp_enable_wizard`
- XPath or positional patches: 1

### `view_totp_form`
- Name: user form: add totp status
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `totp_enabled`
- Buttons: `action_totp_disable`, `action_totp_enable_wizard`
- XPath or positional patches: 1

### `res_users_view_search`
- Name: res.users.view.search.inherit.auth.totp
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/auth_totp/Views]]

<!-- GENERATED:VIEWFILE -->
