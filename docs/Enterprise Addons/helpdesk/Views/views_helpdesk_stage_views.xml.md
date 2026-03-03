---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_stage_views.xml

- Module: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_stage_views.xml`
- Views: 5
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `helpdesk_stage_view_form`
- Name: helpdesk.stage.form
- Model: `helpdesk.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `active`, `color`, `fold`, `name`, `rotting_threshold_days`, `sequence`, `team_ids`, `template_id`, `ticket_count`
- Buttons: `action_open_helpdesk_ticket`
- XPath or positional patches: 0

### `helpdesk_stage_view_kanban`
- Name: helpdesk.stages.kanban
- Model: `helpdesk.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `color`, `name`, `rotting_threshold_days`, `sequence`, `team_ids`
- XPath or positional patches: 0

### `helpdesk_stage_view_search`
- Name: helpdesk.stages.search
- Model: `helpdesk.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `team_ids`, `template_id`
- XPath or positional patches: 0

### `helpdesk_stage_view_tree_inherited`
- Name: helpdesk.stages.tree.inherit
- Model: `helpdesk.stage`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_stage_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `helpdesk_stage_view_tree`
- Name: helpdesk.stages.list
- Model: `helpdesk.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `color`, `fold`, `name`, `rotting_threshold_days`, `sequence`, `team_ids`, `template_id`
- XPath or positional patches: 0

## Actions

- `helpdesk_stage_tree_view_team`: `view`
- `helpdesk_stage_team_action`: `act_window` Team Stages
- `helpdesk_stage_action`: `act_window` Stages
- `unlink_helpdesk_stage_action`: `server` Delete

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk/Views]]

