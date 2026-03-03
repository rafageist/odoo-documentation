---
tags: [odoo, community, generated, views]
---

# views/mail_message_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_message_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_document_file_kanban`
- Name: ir.attachment kanban
- Model: `ir.attachment`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `create_date`, `create_uid`, `id`, `mimetype`, `name`, `type`, `url`
- XPath or positional patches: 0

### `view_message_search`
- Name: mail.message.search
- Model: `mail.message`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `author_id`, `body`, `message_type`, `model`, `parent_id`, `partner_ids`, `res_id`, `subject`
- XPath or positional patches: 0

### `mail_message_view_form`
- Name: mail.message.view.form
- Model: `mail.message`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `author_id`, `body`, `date`, `email_from`, `incoming_email_cc`, `incoming_email_to`, `is_internal`, `is_read`, `mail_server_id`, `message_id`, and 17 more
- Buttons: `action_open_document`
- XPath or positional patches: 0

### `view_message_tree`
- Name: mail.message.list
- Model: `mail.message`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `author_id`, `date`, `model`, `res_id`, `subject`
- XPath or positional patches: 0

## Actions

- `base.action_attachment`: `act_window`
- `action_view_mail_message`: `act_window` Messages

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

