---
tags: [odoo, community, generated, views]
---

# views/discuss_channel_member_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/discuss_channel_member_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `discuss_channel_member_view_form`
- Name: discuss.channel.member.form
- Model: `discuss.channel.member`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `channel_id`, `custom_channel_name`, `custom_notifications`, `fetched_message_id`, `guest_id`, `is_pinned`, `last_interest_dt`, `last_seen_dt`, `message_unread_counter`, `mute_until_dt`, and 4 more
- XPath or positional patches: 0

### `discuss_channel_member_view_tree`
- Name: discuss.channel.member.list
- Model: `discuss.channel.member`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `channel_id`, `guest_id`, `is_pinned`, `last_interest_dt`, `last_seen_dt`, `partner_id`
- XPath or positional patches: 0

## Actions

- `discuss_channel_member_action`: `act_window` Channels/Members

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

