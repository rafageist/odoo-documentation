<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_group_views.xml

- Module: [[docs/Community Addons/mail_group/mail_group|mail_group]]
- Scope: Community Addons
- Source file: `views/mail_group_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_group_view_search`
- Name: mail.group.view.search
- Model: `mail.group`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `alias_email`, `name`
- XPath or positional patches: 0

### `mail_group_view_form`
- Name: mail.group.view.form
- Model: `mail.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `access_group_id`, `access_mode`, `active`, `alias_contact`, `alias_domain_id`, `alias_id`, `alias_name`, `can_manage_group`, `description`, `image_128`, and 13 more
- Buttons: `%(base_setup.action_general_configuration)d`, `%(mail_group.mail_group_member_action)d`, `%(mail_group.mail_group_message_action)d`, `%(mail_group.mail_group_moderation_action)d`, `action_join`, `action_leave`
- XPath or positional patches: 0

### `mail_group_view_kanban`
- Name: mail.group.view.kanban
- Model: `mail.group`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `description`, `image_128`, `is_member`, `mail_group_message_moderation_count`, `name`
- Buttons: `action_join`, `action_leave`
- XPath or positional patches: 0

### `mail_group_view_list`
- Name: mail.group.view.list
- Model: `mail.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `mail_group_message_count`, `mail_group_message_moderation_count`, `member_count`, `name`
- XPath or positional patches: 0

## Actions

- `mail_group_action`: `act_window` Mail Groups

## Navigation

- **Parent:** [[docs/Community Addons/mail_group/Views]]

<!-- GENERATED:VIEWFILE -->
