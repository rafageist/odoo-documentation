<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/crm_lead_views.xml`
- Views: 19
- Actions: 30
- Menus: 0
- Rules: 0

## View records

### `crm_lead_view_search_forecast`
- Name: crm.lead.view.search.forecast
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.view_crm_case_opportunities_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `view_crm_case_opportunities_filter`
- Name: crm.lead.search.opportunity
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `search`
- Field references: 11
- Sample fields: `activity_state`, `city`, `country_id`, `lead_properties`, `name`, `partner_id`, `phone_mobile_search`, `stage_id`, `tag_ids`, `team_id`, and 1 more
- XPath or positional patches: 0

### `crm_lead_view_pivot_forecast`
- Name: crm.lead.view.pivot.forecast
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 14
- Sample fields: `automated_probability`, `color`, `date_deadline`, `day_close`, `day_open`, `message_bounce`, `probability`, `prorated_revenue`, `recurring_revenue`, `recurring_revenue_monthly`, and 4 more
- XPath or positional patches: 0

### `crm_lead_view_pivot`
- Name: crm.lead.view.pivot
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 12
- Sample fields: `automated_probability`, `color`, `create_date`, `expected_revenue`, `message_bounce`, `probability`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, and 2 more
- XPath or positional patches: 0

### `crm_lead_view_graph_forecast`
- Name: crm.lead.view.graph.forecast
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 13
- Sample fields: `automated_probability`, `color`, `date_deadline`, `day_close`, `day_open`, `message_bounce`, `probability`, `prorated_revenue`, `recurring_revenue`, `recurring_revenue_monthly`, and 3 more
- XPath or positional patches: 0

### `crm_lead_view_graph`
- Name: crm.lead.view.graph
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 10
- Sample fields: `automated_probability`, `color`, `message_bounce`, `recurring_revenue`, `recurring_revenue_monthly`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`, `stage_id`, `stage_id_color`, `user_id`
- XPath or positional patches: 0

### `view_crm_case_my_activities_filter`
- Name: crm.lead.search.myactivities
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.view_crm_case_leads_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `crm_lead_view_list_activities`
- Name: crm.lead.list.activities
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `team_id`, `user_id`
- XPath or positional patches: 1

### `crm_lead_view_tree_forecast`
- Name: crm.lead.view.list.forecast
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_tree_view_oppor`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `prorated_revenue`
- XPath or positional patches: 3

### `crm_case_tree_view_oppor`
- Name: crm.lead.list.opportunity
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `list`
- Field references: 39
- Sample fields: `active`, `activity_calendar_event_id`, `activity_ids`, `activity_user_id`, `campaign_id`, `city`, `company_currency`, `company_id`, `contact_name`, `country_id`, and 29 more
- Buttons: `%(crm.action_lead_mail_compose)d`, `%(crm.action_lead_mass_mail)d`, `%(crm.crm_lead_lost_action)d`
- XPath or positional patches: 0

### `view_crm_case_leads_filter`
- Name: crm.lead.search.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `search`
- Field references: 16
- Sample fields: `activity_state`, `activity_type_id`, `activity_user_id`, `campaign_id`, `city`, `country_id`, `create_date`, `lang_id`, `lead_properties`, `medium_id`, and 6 more
- XPath or positional patches: 0

### `crm_lead_view_kanban_forecast`
- Name: crm.lead.view.kanban.forecast
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_case_kanban_view_leads`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `date_deadline`, `prorated_revenue`, `recurring_plan`, `recurring_revenue`, `recurring_revenue_monthly_prorated`, `recurring_revenue_prorated`
- XPath or positional patches: 7

### `crm_case_kanban_view_leads`
- Name: crm.lead.kanban.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 22
- Sample fields: `active`, `activity_ids`, `color`, `company_currency`, `contact_name`, `expected_revenue`, `is_rotting`, `lead_properties`, `name`, `partner_id`, and 12 more
- XPath or positional patches: 0

### `crm_lead_view_activity`
- Name: crm.lead.view.activity
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 7
- Sample fields: `company_currency`, `expected_revenue`, `name`, `partner_id`, `stage_id`, `stage_id_color`, `user_id`
- XPath or positional patches: 0

### `quick_create_opportunity_form`
- Name: crm.lead.form.quick_create
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `form`
- Field references: 26
- Sample fields: `activity_ids`, `city`, `commercial_partner_id`, `company_currency`, `company_id`, `contact_name`, `country_id`, `email_from`, `expected_revenue`, `function`, and 16 more
- XPath or positional patches: 0

### `crm_case_calendar_view_leads`
- Name: crm.lead.calendar.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `expected_revenue`, `lead_properties`, `partner_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `view_crm_lead_kanban`
- Name: crm.lead.kanban
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `activity_ids`, `contact_name`, `name`, `priority`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `crm_case_tree_view_leads`
- Name: crm.lead.list.lead
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `list`
- Field references: 24
- Sample fields: `active`, `campaign_id`, `city`, `company_id`, `contact_name`, `country_id`, `create_date`, `date_deadline`, `email_from`, `medium_id`, and 14 more
- Buttons: `%(crm.crm_lead_lost_action)d`
- XPath or positional patches: 0

### `crm_lead_view_form`
- Name: crm.lead.form
- Model: `crm.lead`
- Type: inferred from arch
- Root tag: `form`
- Field references: 60
- Sample fields: `active`, `automated_probability`, `campaign_id`, `city`, `company_currency`, `company_id`, `contact_name`, `country_id`, `date_closed`, `date_conversion`, and 50 more
- Buttons: `%(crm.action_crm_lead2opportunity_partner)d`, `%(crm.crm_lead_lost_action)d`, `action_restore`, `action_schedule_meeting`, `action_set_won_rainbowman`, `action_show_potential_duplicates`, `mail_action_blacklist_remove`, `phone_action_blacklist_remove`
- XPath or positional patches: 0

## Actions

- `mail_followers_edit_action_from_lead`: `act_window` Add/Remove Followers
- `crm_lead_action_open_lead_form`: `act_window` New Lead
- `crm_lead_action_forecast_view_tree`: `view`
- `crm_lead_action_forecast_view_pivot`: `view`
- `crm_lead_action_forecast_view_graph`: `view`
- `crm_lead_action_forecast_view_kanban`: `view`
- `crm_lead_action_forecast`: `act_window` Forecast
- `crm_lead_action_pipeline_view_graph`: `view`
- `crm_lead_action_pipeline_view_pivot`: `view`
- `crm_lead_action_pipeline_view_calendar`: `view`
- `crm_lead_action_pipeline_view_tree`: `view`
- `crm_lead_action_pipeline_view_kanban`: `view`
- `crm_lead_action_pipeline`: `act_window` Pipeline
- `crm_lead_opportunities_view_calendar`: `view`
- `crm_lead_opportunities_view_pivot`: `view`
- `crm_lead_opportunities_view_graph`: `view`
- `crm_lead_opportunities_view_tree`: `view`
- `crm_lead_opportunities_view_kanban`: `view`
- `crm_lead_opportunities`: `act_window` Opportunities
- `crm_lead_action_my_activities_view_tree`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
