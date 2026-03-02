<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/mail_compose_message_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `wizard/mail_compose_message_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_compose_message_view_form_template_save`
- Name: mail.compose.message.view.form.template.save
- Model: `mail.compose.message`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `model`, `template_name`
- Buttons: `create_mail_template`
- XPath or positional patches: 0

### `email_compose_message_wizard_form`
- Name: mail.compose.message.form
- Model: `mail.compose.message`
- Type: inferred from arch
- Root tag: `form`
- Field references: 38
- Sample fields: `attachment_ids`, `author_id`, `auto_delete`, `auto_delete_keep_log`, `body`, `can_edit_body`, `composition_batch`, `composition_comment_option`, `composition_mode`, `email_from`, and 28 more
- Buttons: `action_schedule_message`, `action_send_mail`
- XPath or positional patches: 0

## Actions

- `action_email_compose_message_wizard`: `act_window` Compose Email

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
