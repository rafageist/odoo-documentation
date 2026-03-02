<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/marketing_campaign_views.xml

- Module: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]]
- Scope: Enterprise Addons
- Source file: `views/marketing_campaign_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `marketing_campaign_view_search`
- Name: marketing.campaign.view.search
- Model: `marketing.campaign`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `model_id`, `name`
- XPath or positional patches: 0

### `marketing_campaign_view_tree`
- Name: marketing.campaign.view.list
- Model: `marketing.campaign`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `link_tracker_click_count`, `mass_mailing_count`, `model_id`, `name`, `state`, `total_participant_count`
- XPath or positional patches: 0

### `marketing_campaign_view_form`
- Name: marketing.campaign.view.form
- Model: `marketing.campaign`
- Type: inferred from arch
- Root tag: `form`
- Field references: 32
- Sample fields: `active`, `activity_type`, `domain`, `interval_number`, `interval_standardized`, `interval_type`, `link_tracker_click_count`, `mailing_filter_count`, `mailing_filter_domain`, `mailing_filter_id`, and 22 more
- Buttons: `%(marketing_campaign_test_action)d`, `%(marketing_participant_action_campaign)d`, `%(marketing_participant_action_campaign_test)d`, `action_set_synchronized`, `action_start_campaign`, `action_stop_campaign`, `action_update_participants`, `action_view_mailings`, `action_view_tracker_statistics`, `execute_activities`, and 1 more
- XPath or positional patches: 0

### `marketing_campaign_view_kanban`
- Name: marketing.campaign.view.kanban
- Model: `marketing.campaign`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `completed_participant_count`, `name`, `running_participant_count`, `total_participant_count`
- XPath or positional patches: 0

## Actions

- `marketing_campaign_action`: `act_window` Campaigns

## Menus

- `marketing_campaign_menu`: Campaigns

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation/Views]]

<!-- GENERATED:VIEWFILE -->
