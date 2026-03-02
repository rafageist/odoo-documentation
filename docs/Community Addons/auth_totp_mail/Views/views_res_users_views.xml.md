<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/auth_totp_mail/auth_totp_mail|auth_totp_mail]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `auth_totp_mail.res_users_view_form`
- Name: res.users.view.form.auth.totp.mail
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `form`
- Field references: 1
- Sample fields: `totp_enabled`
- Buttons: `action_totp_enable_wizard`
- XPath or positional patches: 2

### `view_users_form`
- Name: res.users.view.form.inherit.auth.totp.mail
- Model: `res.users`
- Type: inferred from arch
- Inherits: `auth_totp.view_totp_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_totp_invite`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/auth_totp_mail/Views]]

<!-- GENERATED:VIEWFILE -->
