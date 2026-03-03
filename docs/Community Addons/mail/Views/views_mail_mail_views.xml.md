---
tags: [odoo, community, generated, views]
---

# views/mail_mail_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_mail_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_mail_search`
- Name: mail.mail.search
- Model: `mail.mail`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `author_id`, `date`, `email_from`, `model`, `recipient_ids`, `res_id`
- XPath or positional patches: 0

### `view_mail_tree`
- Name: mail.mail.list
- Model: `mail.mail`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `author_id`, `date`, `email_from`, `message_id`, `message_type`, `model`, `recipient_ids`, `res_id`, `state`, `subject`
- Buttons: `action_retry`, `cancel`, `mark_outgoing`, `send`
- XPath or positional patches: 0

### `view_mail_form`
- Name: mail.mail.form
- Model: `mail.mail`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `author_id`, `auto_delete`, `body_content`, `date`, `email_cc`, `email_from`, `email_to`, `failure_reason`, `fetchmail_server_id`, `headers`, and 15 more
- Buttons: `%(action_email_compose_message_wizard)d`, `action_open_document`, `action_send_and_close`, `cancel`, `mark_outgoing`
- XPath or positional patches: 0

## Actions

- `act_server_history`: `act_window` Messages
- `action_view_mail_mail`: `act_window` Emails

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

