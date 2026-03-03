---
tags: [odoo, community, generated, views]
---

# views/res_users_settings_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/res_users_settings_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_users_settings_view_form`
- Name: res.users.settings.form
- Model: `res.users.settings`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `is_discuss_sidebar_category_channel_open`, `is_discuss_sidebar_category_chat_open`, `partner_id`, `push_to_talk_key`, `use_push_to_talk`, `user_id`, `voice_active_duration`, `volume`, `volume_settings_ids`
- XPath or positional patches: 0

### `res_users_settings_view_tree`
- Name: res.users.settings.list
- Model: `res.users.settings`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `id`, `use_push_to_talk`, `user_id`
- XPath or positional patches: 0

## Actions

- `res_users_settings_action`: `act_window` User Settings

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

