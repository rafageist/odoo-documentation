<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_team_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_team_views.xml`
- Views: 6
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `helpdesk_team_view_kanban_mobile`
- Name: helpdesk.team.view.kanban.mobile
- Model: `helpdesk.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `helpdesk_team_kanban_view`
- Name: helpdesk.team.kanban.view
- Model: `helpdesk.team`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_team_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_team_view_kanban`
- Name: helpdesk.team.dashboard
- Model: `helpdesk.team`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 15
- Sample fields: `alias_email`, `color`, `display_name`, `open_ticket_count`, `rating_avg`, `rating_count`, `sequence`, `sla_failed`, `success_rate`, `ticket_closed`, and 5 more
- Buttons: `action_view_ticket`
- XPath or positional patches: 0

### `helpdesk_team_view_search`
- Name: helpdesk.team.search
- Model: `helpdesk.team`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `helpdesk_team_view_form`
- Name: helpdesk.team.form
- Model: `helpdesk.team`
- Type: inferred from arch
- Root tag: `form`
- Field references: 44
- Sample fields: `access_instruction_message`, `active`, `alias_contact`, `alias_domain_id`, `alias_id`, `alias_name`, `allow_portal_ticket_closing`, `assign_method`, `auto_assignment`, `auto_close_day`, and 34 more
- Buttons: `%(helpdesk.action_helpdesk_tag_assignment)d`, `%(helpdesk.helpdesk_stage_team_action)d`, `action_view_open_ticket_view`, `action_view_sla_policy`, `action_view_team_rating`
- XPath or positional patches: 0

### `helpdesk_team_view_tree`
- Name: helpdesk.team.list
- Model: `helpdesk.team`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `alias_email`, `company_id`, `name`, `sequence`, `use_alias`
- XPath or positional patches: 0

## Actions

- `helpdesk_team_dashboard_action_main`: `act_window` Helpdesk Overview
- `helpdesk_team_action_kanban`: `view`
- `helpdesk_team_action_tree`: `view`
- `helpdesk_team_action`: `act_window` Helpdesk Teams
- `email_template_action_helpdesk`: `act_window` Templates
- `helpdesk_sla_action`: `act_window` SLA Policies

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

<!-- GENERATED:VIEWFILE -->
