<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 22
- Actions: 57
- Menus: 0
- Rules: 0

## View records

### `helpdesk_tickets_view_tree_res_partner`
- Name: helpdesk.ticket.list
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_tickets_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_team_view_graph_analysis`
- Name: helpdesk.ticket.graph
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `close_hours`, `stage_id`, `stage_id_color`, `team_id`
- XPath or positional patches: 0

### `helpdesk_team_view_pivot_analysis`
- Name: helpdesk.ticket.pivot
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `close_hours`, `color`, `name`, `stage_id`, `stage_id_color`
- XPath or positional patches: 0

### `helpdesk_ticket_view_search_analysis`
- Name: helpdesk.ticket.search
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `priority`, `team_id`, `user_id`
- XPath or positional patches: 0

### `helpdesk_ticket_pivot_view_7days_inherit_dashboard`
- Name: helpdesk.ticket.pivot.7days.inherit
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_main`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `close_date`, `close_hours`
- XPath or positional patches: 1

### `helpdesk_ticket_view_graph_7days_inherit_dashboard`
- Name: helpdesk.ticket.graph.7days.inherit
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_graph_main_inherit_all_ticket`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `assign_hours`, `close_date`, `close_hours`, `rating_last_value`
- XPath or positional patches: 1

### `helpdesk_ticket_action_close_analysis_pivot_inherit_dashboard`
- Name: helpdesk.ticket.close.analysis.pivot.inherit
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_pivot_main`
- Root tag: `field`
- Field references: 2
- Sample fields: `name`, `stage_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_pivot_main_inherit_all_ticket`
- Name: helpdesk.ticket.pivot.inherit.all.ticket
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_pivot_main`
- Root tag: `field`
- Field references: 4
- Sample fields: `answered_customer_message_count`, `create_date`, `stage_id`, `total_response_hours`
- XPath or positional patches: 0

### `helpdesk_ticket_view_graph_main_inherit_all_ticket`
- Name: helpdesk.ticket.graph.inherit.all.ticket
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_graph_main`
- Root tag: `field`
- Field references: 5
- Sample fields: `answered_customer_message_count`, `stage_id`, `team_id`, `total_response_hours`, `user_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_cohort`
- Name: helpdesk.ticket.view.cohort
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 2
- Sample fields: `color`, `stage_id_color`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form`
- Name: helpdesk.ticket.form
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `form`
- Field references: 33
- Sample fields: `active`, `company_id`, `description`, `display_extra_info`, `domain_user_ids`, `email_cc`, `fold`, `is_partner_phone_update`, `is_rotting`, `kanban_state`, and 23 more
- Buttons: `action_open_helpdesk_ticket`, `action_open_ratings`
- XPath or positional patches: 0

### `helpdesk_ticket_view_kanban`
- Name: helpdesk.ticket.kanban
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 21
- Sample fields: `active`, `activity_ids`, `activity_state`, `color`, `commercial_partner_id`, `fold`, `is_rotting`, `kanban_state`, `name`, `priority`, and 11 more
- XPath or positional patches: 0

### `quick_create_ticket_form`
- Name: helpdesk.ticket.form.quick_create
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `domain_user_ids`, `legend_blocked`, `legend_done`, `legend_normal`, `name`, `partner_id`, `stage_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `ticket_pivot_view_group_stage`
- Name: helpdesk.ticket.pivot.group.stage
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_main`
- Root tag: `field`
- Field references: 2
- Sample fields: `stage_id`, `user_id`
- XPath or positional patches: 0

### `ticket_list_view_group_stage`
- Name: helpdesk.ticket.list.group.stage
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_tickets_view_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_tickets_view_tree`
- Name: helpdesk.ticket.list
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `list`
- Field references: 26
- Sample fields: `activity_ids`, `company_id`, `create_date`, `fold`, `is_rotting`, `kanban_state`, `legend_blocked`, `legend_done`, `legend_normal`, `my_activity_date_deadline`, and 16 more
- XPath or positional patches: 0

### `helpdesk_ticket_view_search_analysis_closed`
- Name: helpdesk.ticket.search
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `team_id`, `user_id`
- XPath or positional patches: 0

### `helpdesk_tickets_view_search`
- Name: helpdesk.ticket.search
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_tickets_view_search_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `company_id`, `properties`
- XPath or positional patches: 4

### `helpdesk_tickets_view_search_base`
- Name: helpdesk.ticket.search.base
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `company_id`, `name`, `partner_id`, `priority`, `sla_ids`, `stage_id`, `tag_ids`, `team_id`, `user_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_pivot_main`
- Name: helpdesk.ticket.pivot
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 8
- Sample fields: `answered_customer_message_count`, `assign_hours`, `close_hours`, `color`, `rating_last_value`, `stage_id`, `stage_id_color`, `total_response_hours`
- XPath or positional patches: 0

### `helpdesk_ticket_view_graph_main`
- Name: helpdesk.ticket.graph
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 12
- Sample fields: `answered_customer_message_count`, `assign_hours`, `avg_response_hours`, `close_hours`, `color`, `first_response_hours`, `rating_last_value`, `sla_deadline_hours`, `stage_id`, `stage_id_color`, and 2 more
- XPath or positional patches: 0

### `helpdesk_ticket_view_activity`
- Name: helpdesk.ticket.activity
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 7
- Sample fields: `legend_blocked`, `legend_done`, `legend_normal`, `name`, `partner_id`, `ticket_ref`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_edit_followers_helpdesk_ticket`: `act_window` Add/remove followers
- `helpdesk_ticket_action_7days_success_graph`: `view`
- `helpdesk_ticket_action_7days_success_pivot`: `view`
- `helpdesk_ticket_action_7days_success_activity`: `view`
- `helpdesk_ticket_action_7days_success_kanban`: `view`
- `helpdesk_ticket_action_7days_success_tree`: `view`
- `helpdesk_ticket_action_7days_success`: `act_window` Success Rate
- `action_open_customer_preview`: `server` Preview
- `helpdesk_ticket_action_success_pivot`: `view`
- `helpdesk_ticket_action_success_graph`: `view`
- `helpdesk_ticket_action_success_tree`: `view`
- `helpdesk_ticket_action_success`: `act_window` Success Rate Analysis
- `helpdesk_ticket_action_team_performance`: `act_window` Performance Analysis
- `helpdesk_ticket_action_unassigned`: `act_window` Tickets
- `open_view_ticket_group_stage_pivot_view`: `view`
- `open_view_ticket_group_stage_activity_view`: `view`
- `open_view_ticket_group_stage_tree_view`: `view`
- `open_view_ticket_group_stage_kanban_view`: `view`
- `helpdesk_ticket_action_team`: `act_window` Tickets
- `helpdesk_ticket_action_7days_tickets_cohort`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

<!-- GENERATED:VIEWFILE -->
