---
tags: [odoo, community, generated, views]
---

# views/fetchmail_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/fetchmail_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_email_server_search`
- Name: fetchmail.server.search
- Model: `fetchmail.server`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `user`
- XPath or positional patches: 0

### `view_email_server_form`
- Name: fetchmail.server.form
- Model: `fetchmail.server`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `active`, `attach`, `configuration`, `date`, `error_date`, `error_message`, `is_ssl`, `name`, `object_id`, `original`, and 9 more
- Buttons: `button_confirm_login`, `fetch_mail`, `set_draft`
- XPath or positional patches: 0

### `view_email_server_tree`
- Name: fetchmail.server.list
- Model: `fetchmail.server`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `date`, `name`, `server_type`, `state`, `user`
- XPath or positional patches: 0

## Actions

- `action_email_server_tree`: `act_window` Incoming Mail Servers

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

