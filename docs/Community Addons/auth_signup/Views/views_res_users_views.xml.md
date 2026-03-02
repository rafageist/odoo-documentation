<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/auth_signup/auth_signup|auth_signup]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_users_state_tree`
- Name: res.users.list.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_tree`
- Root tag: `list`
- Field references: 1
- Sample fields: `state`
- XPath or positional patches: 1

### `res_users_view_form`
- Name: res.users.form.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `state`
- Buttons: `action_reset_password`
- XPath or positional patches: 2

## Actions

- `action_send_password_reset_instructions`: `server` Send Password Reset Instructions

## Navigation

- **Parent:** [[docs/Community Addons/auth_signup/Views]]

<!-- GENERATED:VIEWFILE -->
