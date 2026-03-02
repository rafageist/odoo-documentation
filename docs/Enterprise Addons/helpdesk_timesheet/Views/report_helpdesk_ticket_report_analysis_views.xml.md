<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/helpdesk_ticket_report_analysis_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]]
- Scope: Enterprise Addons
- Source file: `report/helpdesk_ticket_report_analysis_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_helpdesk_ticket_pivot_analysis`
- Name: helpdesk.ticket.report.analysis.pivot.inherited
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_analysis`
- Root tag: `field`
- Field references: 2
- Sample fields: `ticket_open_hours`, `total_hours_spent`
- XPath or positional patches: 0

### `view_helpdesk_ticket_graph_analysis`
- Name: helpdesk.ticket.report.analysis.inherited
- Model: `helpdesk.ticket.report.analysis`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_graph_analysis`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
