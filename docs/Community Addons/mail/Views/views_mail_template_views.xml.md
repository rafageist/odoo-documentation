---
tags: [odoo, community, generated, views]
---

# views/mail_template_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_template_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_email_template_search`
- Name: email.template.search
- Model: `mail.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `lang`, `model`, `model_id`, `name`
- XPath or positional patches: 0

### `email_template_tree`
- Name: email.template.list
- Model: `mail.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `description`, `email_from`, `email_to`, `mail_server_id`, `model_id`, `name`, `partner_to`, `subject`, `user_id`
- XPath or positional patches: 0

### `email_template_form`
- Name: email.template.form
- Model: `mail.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `attachment_ids`, `auto_delete`, `body_html`, `can_write`, `description`, `email_cc`, `email_from`, `email_to`, `has_dynamic_reports`, `has_mail_server`, and 15 more
- Buttons: `%(mail_template_reset_action)d`, `action_open_mail_preview`, `create_action`, `unlink_action`
- XPath or positional patches: 0

## Actions

- `action_email_template_tree_all`: `act_window` Email Templates

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

