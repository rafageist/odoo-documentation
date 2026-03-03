---
tags: [odoo, community, generated, views]
---

# views/discuss_channel_rtc_session_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/discuss_channel_rtc_session_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `discuss_channel_rtc_session_view_form`
- Name: discuss.channel.rtc.session.form
- Model: `discuss.channel.rtc.session`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `channel_id`, `channel_member_id`, `guest_id`, `is_camera_on`, `is_deaf`, `is_muted`, `is_screen_sharing_on`, `partner_id`
- XPath or positional patches: 0

### `discuss_channel_rtc_session_view_tree`
- Name: discuss.channel.rtc.session.list
- Model: `discuss.channel.rtc.session`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `channel_id`, `channel_member_id`, `id`, `write_date`
- Buttons: `action_disconnect`
- XPath or positional patches: 0

### `discuss_channel_rtc_session_view_search`
- Name: discuss.channel.rtc.session.search
- Model: `discuss.channel.rtc.session`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `channel_member_id`
- XPath or positional patches: 0

## Actions

- `discuss_channel_rtc_session_action`: `act_window` RTC sessions

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

