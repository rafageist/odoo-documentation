<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_timesheet/helpdesk_timesheet|helpdesk_timesheet]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_graph_main_inherit_helpdesk_timesheet`
- Name: helpdesk.ticket.graph.inherit.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_graph_main`
- Root tag: `field`
- Field references: 2
- Sample fields: `assign_hours`, `total_hours_spent`
- XPath or positional patches: 0

### `helpdesk_ticket_view_pivot_main_inherit_helpdesk_timesheet`
- Name: helpdesk.ticket.pivot.inherit.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_pivot_main`
- Root tag: `field`
- Field references: 2
- Sample fields: `assign_hours`, `total_hours_spent`
- XPath or positional patches: 0

### `helpdesk_ticket_view_tree_inherit_helpdesk_timesheet`
- Name: helpdesk.ticket.list.inherit.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_tickets_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `analytic_account_id`, `partner_id`, `total_hours_spent`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form_inherit_helpdesk_timesheet_restrict_teams`
- Name: helpdesk.ticket.form.inherit.timesheet.restrict.teams
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_timesheet.helpdesk_ticket_view_form_inherit_helpdesk_timesheet`
- Root tag: `field`
- Field references: 1
- Sample fields: `team_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form_inherit_helpdesk_timesheet`
- Name: helpdesk.ticket.form.inherit.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 17
- Sample fields: `analytic_account_id`, `company_id`, `date`, `display_timesheet_timer`, `employee_id`, `encode_uom_in_days`, `name`, `project_id`, `readonly_timesheet`, `stage_id`, and 7 more
- Buttons: `action_timer_start`, `action_timer_stop`
- XPath or positional patches: 4

## Actions

- `project_project_action_view_helpdesk_tickets`: `act_window` Tickets

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
