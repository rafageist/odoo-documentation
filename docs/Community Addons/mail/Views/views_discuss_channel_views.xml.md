<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/discuss_channel_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/discuss_channel_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `mail.discuss_channel_view_search`
- Name: discuss.channel.search
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mail.discuss_channel_view_tree`
- Name: discuss.channel.list
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mail.discuss_channel_view_form`
- Name: discuss.channel.form
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `active`, `avatar_128`, `channel_member_ids`, `channel_type`, `description`, `from_message_id`, `group_ids`, `group_public_id`, `guest_id`, `image_128`, and 7 more
- XPath or positional patches: 0

### `mail.discuss_channel_view_list`
- Name: discuss.channel.list
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `avatar_128`, `description`, `name`
- Buttons: `action_unfollow`, `channel_join`
- XPath or positional patches: 0

### `mail.discuss_channel_view_kanban`
- Name: discuss.channel.kanban
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `active`, `avatar_128`, `channel_type`, `description`, `group_ids`, `is_member`, `name`
- Buttons: `action_unfollow`, `channel_join`
- XPath or positional patches: 0

## Actions

- `mail.action_discuss`: `client` Discuss
- `mail.discuss_channel_action`: `act_window` Channels
- `mail.discuss_channel_action_view`: `act_window` Join a group

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
