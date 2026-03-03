---
tags: [odoo, enterprise, generated, views]
---

# views/marketing_participant_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]]
- Scope: Enterprise Addons
- Source file: `views/marketing_participant_views.xml`
- Views: 5
- Actions: 4
- Menus: 1
- Rules: 0

## View records

### `marketing_participant_view_pivot`
- Name: marketing.participant.view.pivot
- Model: `marketing.participant`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `campaign_id`, `state`
- XPath or positional patches: 0

### `marketing_participant_view_graph`
- Name: marketing.participant.view.graph
- Model: `marketing.participant`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `model_id`, `state`
- XPath or positional patches: 0

### `marketing_participant_view_search`
- Name: marketing.participant.view.search
- Model: `marketing.participant`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `campaign_id`, `resource_ref`
- XPath or positional patches: 0

### `marketing_participant_view_tree`
- Name: marketing.participant.view.list
- Model: `marketing.participant`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `campaign_id`, `is_test`, `model_id`, `resource_ref`, `state`
- XPath or positional patches: 0

### `marketing_participant_view_form`
- Name: marketing.participant.view.form
- Model: `marketing.participant`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `activity_id`, `activity_type`, `campaign_id`, `create_date`, `is_test`, `links_click_datetime`, `mailing_trace_status`, `model_id`, `parent_id`, `res_id`, and 6 more
- Buttons: `action_execute`, `action_set_completed`, `participant_action_cancel`
- XPath or positional patches: 0

## Actions

- `marketing_participant_action_campaign_test`: `act_window` Participants
- `marketing_participant_action_campaign`: `act_window` Participants
- `marketing_participants_action_mail`: `act_window` Participants
- `marketing_participants_action_reporting`: `act_window` Participants

## Menus

- `marketing_participants_menu`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation/Views]]

