---
tags: [odoo, community, generated, views]
---

# views/event_track_stage_views.xml

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `views/event_track_stage_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_event_track_stage_kanban`
- Name: event.track.stage.kanban
- Model: `event.track.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `event_track_stage_view_tree`
- Name: event.track.stage.view.list
- Model: `event.track.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `fold`, `is_cancel`, `is_fully_accessible`, `is_visible_in_agenda`, `name`, `sequence`
- XPath or positional patches: 0

### `event_track_stage_view_form`
- Name: event.track.stage.view.form
- Model: `event.track.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `color`, `description`, `fold`, `is_cancel`, `is_fully_accessible`, `is_visible_in_agenda`, `legend_blocked`, `legend_done`, `legend_normal`, `mail_template_id`, and 1 more
- XPath or positional patches: 0

### `event_track_stage_view_search`
- Name: event.track.stage.view.search
- Model: `event.track.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `event_track_stage_action`: `act_window` Track Stages

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Views]]

