<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/discuss_channel_views.xml

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `views/discuss_channel_views.xml`
- Views: 9
- Actions: 16
- Menus: 0
- Rules: 0

## View records

### `discuss_channel_looking_for_help_view_kanban`
- Name: discuss.channel.kanban
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `country_id`, `create_date`, `livechat_agent_partner_ids`, `livechat_customer_history_ids`, `livechat_expertise_ids`, `livechat_lang_id`
- XPath or positional patches: 0

### `discuss_channel_looking_for_help_view_list`
- Name: discuss.channel.looking.for.help.list
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `country_id`, `create_date`, `description`, `duration`, `livechat_agent_history_ids`, `livechat_bot_history_ids`, `livechat_channel_id`, `livechat_conversation_tag_ids`, `livechat_customer_history_ids`, `livechat_expertise_ids`, and 2 more
- XPath or positional patches: 0

### `discuss_channel_looking_for_help_view_search`
- Name: discuss.channel.looking.for.help.view.search
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `country_id`, `description`, `livechat_agent_partner_ids`, `livechat_bot_partner_ids`, `livechat_conversation_tag_ids`, `livechat_customer_partner_ids`, `livechat_expertise_ids`, `livechat_lang_id`
- XPath or positional patches: 0

### `discuss_channel_view_graph`
- Name: discuss.channel.graph
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `create_date`, `rating_last_value`
- XPath or positional patches: 0

### `discuss_channel_view_pivot`
- Name: discuss.channel.pivot
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `create_date`, `livechat_operator_id`, `rating_last_value`
- XPath or positional patches: 0

### `discuss_channel_view_form`
- Name: discuss.channel.form
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `create_date`, `name`, `rating_last_feedback`, `rating_last_image`
- XPath or positional patches: 0

### `discuss_channel_view_kanban`
- Name: discuss.channel.kanban
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `country_id`, `create_date`, `duration`, `livechat_agent_partner_ids`, `livechat_customer_history_ids`, `livechat_failure`, `livechat_is_escalated`, `message_count`, `rating_last_image`
- XPath or positional patches: 0

### `discuss_channel_view_tree`
- Name: discuss.channel.list
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `country_id`, `create_date`, `duration`, `livechat_agent_history_ids`, `livechat_agent_providing_help_history`, `livechat_agent_requesting_help_history`, `livechat_bot_history_ids`, `livechat_channel_id`, `livechat_conversation_tag_ids`, `livechat_customer_history_ids`, and 5 more
- XPath or positional patches: 0

### `discuss_channel_view_search`
- Name: discuss.channel.search
- Model: `discuss.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `country_id`, `livechat_agent_partner_ids`, `livechat_agent_providing_help_history`, `livechat_agent_requesting_help_history`, `livechat_customer_partner_ids`
- XPath or positional patches: 0

## Actions

- `discuss_channel_looking_for_help_action_form`: `view`
- `discuss_channel_looking_for_help_action_kanban`: `view`
- `discuss_channel_looking_for_help_action_list`: `view`
- `discuss_channel_looking_for_help_action`: `act_window` Looking for Help
- `discuss_channel_action_livechat_form`: `view`
- `discuss_channel_action_livechat_graph`: `view`
- `discuss_channel_action_livechat_pivot`: `view`
- `discuss_channel_action_livechat_tree`: `view`
- `discuss_channel_action_livechat_kanban`: `view`
- `discuss_channel_action_from_livechat_channel`: `act_window` Sessions
- `discuss_channel_action_form`: `view`
- `discuss_channel_action_graph`: `view`
- `discuss_channel_action_pivot`: `view`
- `discuss_channel_action_tree`: `view`
- `discuss_channel_action_kanban`: `view`
- `discuss_channel_action`: `act_window` Sessions

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Views]]

<!-- GENERATED:VIEWFILE -->
