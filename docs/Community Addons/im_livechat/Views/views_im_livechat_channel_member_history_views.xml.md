<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/im_livechat_channel_member_history_views.xml

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `views/im_livechat_channel_member_history_views.xml`
- Views: 5
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `im_livechat_agent_history_view_pivot`
- Name: im_livechat.agent.history.pivot
- Model: `im_livechat.channel.member.history`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 10
- Sample fields: `call_count`, `call_duration_hour`, `call_percentage`, `has_call`, `partner_id`, `rating`, `response_time_hour`, `session_duration_hour`, `session_start_hour`, `session_week_day`
- XPath or positional patches: 0

### `im_livechat_agent_history_view_graph`
- Name: im_livechat.agent.history.graph
- Model: `im_livechat.channel.member.history`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 8
- Sample fields: `call_duration_hour`, `call_percentage`, `has_call`, `rating`, `response_time_hour`, `session_duration_hour`, `session_start_hour`, `session_week_day`
- XPath or positional patches: 0

### `im_livechat_agent_history_view_search`
- Name: im_livechat.agent.history.search
- Model: `im_livechat.channel.member.history`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `agent_expertise_ids`, `conversation_tag_ids`, `partner_id`, `session_country_id`, `session_livechat_channel_id`
- XPath or positional patches: 0

### `im_livechat_channel_member_history_view_tree`
- Name: im_livechat.channel.member.history.view.list
- Model: `im_livechat.channel.member.history`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `channel_id`, `chatbot_script_id`, `create_date`, `guest_id`, `livechat_member_type`, `partner_id`, `session_duration_hour`
- XPath or positional patches: 0

### `im_livechat_channel_member_history_view_search`
- Name: im_livechat.channel.member.history.view.search
- Model: `im_livechat.channel.member.history`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `channel_id`, `chatbot_script_id`, `guest_id`, `livechat_member_type`, `partner_id`
- XPath or positional patches: 0

## Actions

- `im_livechat_agent_history_action`: `act_window` Agents
- `im_livechat_channel_member_history_action`: `act_window` Member History

## Menus

- `menu_reporting_livechat_agent`: Agents
- `im_livechat.menu_member_history`: Member History

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Views]]

<!-- GENERATED:VIEWFILE -->
