---
tags: [odoo, enterprise, generated, views]
---

# report/helpdesk_sla_report_analysis_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `report/helpdesk_sla_report_analysis_views.xml`
- Views: 6
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `helpdesk_sla_report_analysis_view_search`
- Name: helpdesk.sla.report.analysis.search
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk_tickets_view_search_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 2

### `helpdesk_sla_report_analysis_view_cohort`
- Name: helpdesk.sla.report.analysis.cohort
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 0
- XPath or positional patches: 0

### `helpdesk_sla_report_graph_analysis_dashboard`
- Name: helpdesk.sla.report.graph.analysis.dashboard
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_sla_report_analysis_view_graph`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_sla_report_analysis_view_graph`
- Name: helpdesk.sla.report.analysis.graph
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 5
- Sample fields: `sla_exceeded_hours`, `sla_id`, `sla_status`, `ticket_assignation_hours`, `ticket_close_hours`
- XPath or positional patches: 0

### `helpdesk_sla_report_analysis_view_pivot_dashboard`
- Name: helpdesk.sla.report.analysis.pivot.dashboard
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_sla_report_analysis_view_pivot`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_sla_report_analysis_view_pivot`
- Name: helpdesk.sla.report.analysis.pivot
- Model: `helpdesk.sla.report.analysis`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 11
- Sample fields: `avg_response_hours`, `first_response_hours`, `rating_avg`, `sla_exceeded_hours`, `sla_id`, `sla_status`, `sla_status_failed`, `team_id`, `ticket_assignation_hours`, `ticket_close_hours`, and 1 more
- XPath or positional patches: 0

## Actions

- `helpdesk_sla_report_analysis_dashboard_graph_view`: `view`
- `helpdesk_sla_report_analysis_dashboard_pivot_view`: `view`
- `helpdesk_sla_report_analysis_dashboard_action`: `act_window` SLA Status Analysis
- `action_appraisal_view_report_cohort`: `view`
- `action_appraisal_view_report_graph`: `view`
- `action_appraisal_view_report_pivot`: `view`
- `helpdesk_sla_report_analysis_action`: `act_window` SLA Status Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

