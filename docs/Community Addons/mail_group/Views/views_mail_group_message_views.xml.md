<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_group_message_views.xml

- Module: [[docs/Community Addons/mail_group/mail_group|mail_group]]
- Scope: Community Addons
- Source file: `views/mail_group_message_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_group_message_view_search`
- Name: mail.group.message.view.search
- Model: `mail.group.message`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `author_id`, `email_from`, `mail_group_id`, `moderation_status`
- XPath or positional patches: 0

### `mail_group_message_view_form`
- Name: mail.group.message.view.form
- Model: `mail.group.message`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `attachment_ids`, `author_id`, `author_moderation`, `body`, `create_date`, `email_from`, `is_group_moderated`, `mail_group_id`, `mail_message_id`, `moderation_status`, and 1 more
- Buttons: `%(mail_group_message_reject_action)d`, `action_moderate_accept`, `action_moderate_allow`
- XPath or positional patches: 0

### `mail_group_message_view_list`
- Name: mail.group.message.view.list
- Model: `mail.group.message`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `author_id`, `create_date`, `email_from`, `is_group_moderated`, `mail_group_id`, `moderation_status`, `subject`
- Buttons: `%(mail_group_message_reject_action)d`, `action_moderate_accept`, `action_moderate_allow`
- XPath or positional patches: 0

## Actions

- `mail_group_message_action`: `act_window` Messages

## Navigation

- **Parent:** [[docs/Community Addons/mail_group/Views]]

<!-- GENERATED:VIEWFILE -->
