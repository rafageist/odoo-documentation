<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/im_livechat_channel_views.xml

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `views/im_livechat_channel_views.xml`
- Views: 6
- Actions: 1
- Menus: 11
- Rules: 0

## View records

### `im_livechat_channel_rule_view_form`
- Name: im_livechat.channel.rule.form
- Model: `im_livechat.channel.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `action`, `auto_popup_timer`, `chatbot_enabled_condition`, `chatbot_script_id`, `country_ids`, `regex_url`
- XPath or positional patches: 0

### `im_livechat_channel_rule_view_kanban`
- Name: im_livechat.channel.rule.kanban
- Model: `im_livechat.channel.rule`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `action`, `country_ids`, `regex_url`
- XPath or positional patches: 0

### `im_livechat_channel_rule_view_tree`
- Name: im.livechat.channel.rule.list
- Model: `im_livechat.channel.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `action`, `chatbot_script_id`, `country_ids`, `regex_url`, `sequence`
- XPath or positional patches: 0

### `im_livechat_channel_view_search`
- Name: im.livechat.channel.view.search
- Model: `im_livechat.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `im_livechat_channel_view_form`
- Name: im_livechat.channel.form
- Model: `im_livechat.channel`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `are_you_inside`, `avatar_1024`, `block_assignment_during_call`, `button_background_color`, `button_text`, `button_text_color`, `chatbot_script_count`, `default_message`, `header_background_color`, `livechat_expertise_ids`, and 18 more
- Buttons: `%(discuss_channel_action_from_livechat_channel)d`, `action_join`, `action_quit`, `action_view_chatbot_scripts`
- XPath or positional patches: 0

### `im_livechat_channel_view_kanban`
- Name: im_livechat.channel.kanban
- Model: `im_livechat.channel`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `are_you_inside`, `available_operator_ids`, `name`, `nbr_channel`, `rating_count`, `rating_percentage_satisfaction`
- Buttons: `action_join`, `action_quit`
- XPath or positional patches: 0

## Actions

- `im_livechat_channel_action`: `act_window` Live Chat Channels

## Menus

- `menu_livechat_conversation_tag`: Tags
- `chatbot_config`: Chatbots
- `canned_responses`: Canned Responses
- `livechat_technical`: Technical
- `livechat_config`: Configuration
- `menu_reporting_livechat`: Reporting
- `menu_livechat_looking_for_help`: Looking for Help
- `menu_livechat_all_conversations`: All Conversations
- `menu_livechat_sessions`: Sessions
- `support_channels`: Channels
- `menu_livechat_root`: Live Chat

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Views]]

<!-- GENERATED:VIEWFILE -->
