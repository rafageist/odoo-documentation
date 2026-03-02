<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_sla_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_sla_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `helpdesk_sla_view_form`
- Name: helpdesk.sla.form
- Model: `helpdesk.sla`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `active`, `company_id`, `description`, `exclude_stage_ids`, `name`, `partner_ids`, `priority`, `stage_id`, `tag_ids`, `team_id`, and 2 more
- Buttons: `action_open_helpdesk_ticket`
- XPath or positional patches: 0

### `helpdesk_sla_view_search`
- Name: helpdesk.sla.search
- Model: `helpdesk.sla`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `team_id`
- XPath or positional patches: 0

### `helpdesk_sla_view_kanban`
- Name: helpdesk.sla.kanban
- Model: `helpdesk.sla`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `team_id`
- XPath or positional patches: 0

### `helpdesk_sla_view_tree`
- Name: helpdesk.sla.list
- Model: `helpdesk.sla`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `exclude_stage_ids`, `name`, `partner_ids`, `priority`, `stage_id`, `tag_ids`, `team_id`, `time`
- XPath or positional patches: 0

## Actions

- `helpdesk_sla_action_main`: `act_window` SLA Policies

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

<!-- GENERATED:VIEWFILE -->
