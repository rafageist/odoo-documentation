<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/im_livechat_report_channel_views.xml

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `report/im_livechat_report_channel_views.xml`
- Views: 5
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `im_livechat_report_channel_view_search`
- Name: im_livechat.report.channel.search
- Model: `im_livechat.report.channel`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `agent_requesting_help_history`, `chatbot_answers_path_str`, `chatbot_script_id`, `conversation_tag_ids`, `country_id`, `livechat_channel_id`, `partner_id`, `session_expertises`, `visitor_partner_id`
- XPath or positional patches: 0

### `im_livechat_report_channel_view_graph`
- Name: im_livechat.report.channel.graph
- Model: `im_livechat.report.channel`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `call_duration_hour`, `has_call`, `percentage_of_calls`, `rating`, `rating_text`, `start_date`
- XPath or positional patches: 0

### `im_livechat_report_channel_view_form`
- Name: im_livechat.report.channel.form
- Model: `im_livechat.report.channel`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `channel_name`
- XPath or positional patches: 0

### `im_livechat_report_channel_view_list`
- Name: im_livechat.report.channel.list
- Model: `im_livechat.report.channel`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `channel_name`, `country_id`, `duration`, `lang_id`, `nbr_message`, `rating_text`, `session_expertise_ids`, `start_date`
- XPath or positional patches: 0

### `im_livechat_report_channel_view_pivot`
- Name: im_livechat.report.channel.pivot
- Model: `im_livechat.report.channel`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 8
- Sample fields: `call_duration_hour`, `duration`, `has_call`, `number_of_calls`, `partner_id`, `percentage_of_calls`, `rating`, `time_to_answer`
- XPath or positional patches: 0

## Actions

- `im_livechat_report_channel_time_to_answer_action`: `act_window` Sessions
- `im_livechat_report_channel_action`: `act_window` Sessions

## Menus

- `menu_reporting_livechat_channel`: Sessions

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Views]]

<!-- GENERATED:VIEWFILE -->
