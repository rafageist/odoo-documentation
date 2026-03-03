---
tags: [odoo, community, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_users_form_mail`
- Name: res.users.form.mail
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `data`
- Field references: 7
- Sample fields: `notification_type`, `out_of_office_from`, `out_of_office_message`, `out_of_office_to`, `outgoing_mail_server_id`, `outgoing_mail_server_type`, `signature`
- XPath or positional patches: 2

### `view_users_form_simple_modif_mail`
- Name: res.users.preferences.form.mail
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form_simple_modif`
- Root tag: `data`
- Field references: 7
- Sample fields: `notification_type`, `out_of_office_from`, `out_of_office_message`, `out_of_office_to`, `outgoing_mail_server_id`, `outgoing_mail_server_type`, `signature`
- XPath or positional patches: 2

## Actions

- `action_res_users_my_fullpage_view`: `view`
- `action_res_users_my_fullpage`: `act_window` Change My Preferences

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

