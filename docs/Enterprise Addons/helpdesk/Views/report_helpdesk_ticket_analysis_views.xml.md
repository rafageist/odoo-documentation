<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/helpdesk_ticket_analysis_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `report/helpdesk_ticket_analysis_views.xml`
- Views: 13
- Actions: 13
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_report_analysis_view_search`
- Name: helpdesk.ticket.report.analysis.search
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk_tickets_view_search_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_report_analysis_view_tree`
- Name: helpdesk.ticket.report.analysis.list
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `partner_id`, `priority`, `stage_id`, `team_id`, `ticket_id`
- XPath or positional patches: 0

### `helpdesk_ticket_report_view_cohort`
- Name: helpdesk.ticket.report.analysis.cohort
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 0
- XPath or positional patches: 0

### `helpdesk_ticket_view_graph_analysis_inherit_dashboard`
- Name: helpdesk.ticket.view.graph.analysis.inherit
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_graph_analysis`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `create_date`, `stage_id`
- XPath or positional patches: 2

### `helpdesk_ticket_view_graph_analysis_dashboard`
- Name: helpdesk.ticket.view.graph.analysis.dashboard
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_graph_analysis`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_view_graph_analysis`
- Name: helpdesk.ticket.report.analysis.graph
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 9
- Sample fields: `avg_response_hours`, `first_response_hours`, `rating_avg`, `stage_id`, `team_id`, `ticket_assignation_hours`, `ticket_close_hours`, `ticket_deadline_hours`, `ticket_open_hours`
- XPath or positional patches: 0

### `helpdesk_ticket_view_list_analysis`
- Name: helpdesk.ticket.report.analysis.list
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `company_id`, `partner_id`, `priority`, `sla_deadline`, `stage_id`, `team_id`, `ticket_id`, `user_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_pivot_analysis_inherit_dashboard`
- Name: helpdesk.ticket.view.pivot.analysis.inherit
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_pivot_analysis_7dayssuccess_inherit_dashboard`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `create_date`, `ticket_open_hours`
- XPath or positional patches: 1

### `helpdesk_ticket_view_pivot_analysis_7dayssuccess_inherit_dashboard`
- Name: helpdesk.ticket.view.pivot.analysis.7dayssuccess.inherit
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_pivot_7days_analysis_inherit_dashboard`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_view_pivot_analysis_success_inherit_dashboard`
- Name: helpdesk.ticket.view.pivot.analysis.success.inherit
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk_ticket_view_pivot_7days_analysis_inherit_dashboard`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `ticket_id`
- XPath or positional patches: 1

### `helpdesk_ticket_view_pivot_7days_analysis_inherit_dashboard`
- Name: helpdesk.ticket.view.pivot.7days.analysis.inherit
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_analysis`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `close_date`, `ticket_assignation_hours`, `ticket_close_hours`, `ticket_open_hours`
- XPath or positional patches: 1

### `helpdesk_ticket_view_pivot_analysis_dashboard`
- Name: helpdesk.ticket.report.analysis.pivot.dashboard
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_analysis`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_view_pivot_analysis`
- Name: helpdesk.ticket.report.analysis.pivot
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 8
- Sample fields: `avg_response_hours`, `first_response_hours`, `rating_avg`, `team_id`, `ticket_assignation_hours`, `ticket_close_hours`, `ticket_deadline_hours`, `ticket_open_hours`
- XPath or positional patches: 0

## Actions

- `helpdesk_ticket_action_dashboard_graph`: `view`
- `helpdesk_ticket_action_dashboard_pivot`: `view`
- `helpdesk_ticket_action_dashboard`: `act_window` Ticket Analysis
- `helpdesk_ticket_action_7dayssuccess_graph`: `view`
- `helpdesk_ticket_action_7dayssuccess_pivot`: `view`
- `helpdesk_ticket_action_7dayssuccess`: `act_window` Success Rate Analysis
- `action_helpdesk_ticket_analysis_dashboard_pivot_view`: `view`
- `action_helpdesk_ticket_analysis_dashboard_graph_view`: `view`
- `helpdesk_ticket_analysis_dashboard_action`: `act_window` Ticket Analysis
- `action_helpdesk_ticket_analysis_cohort`: `view`
- `action_helpdesk_ticket_analysis_pivot`: `view`
- `action_helpdesk_ticket_analysis_graph`: `view`
- `helpdesk_ticket_analysis_action`: `act_window` Tickets Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

<!-- GENERATED:VIEWFILE -->
