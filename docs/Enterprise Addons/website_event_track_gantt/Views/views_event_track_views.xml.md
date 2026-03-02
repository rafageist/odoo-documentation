<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/event_track_views.xml

- Module: [[docs/Enterprise Addons/website_event_track_gantt/website_event_track_gantt|website_event_track_gantt]]
- Scope: Enterprise Addons
- Source file: `views/event_track_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `event_track_view_gantt`
- Name: event.track.view.gantt
- Model: `event.track`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 1
- Sample fields: `partner_name`
- XPath or positional patches: 0

### `event_track_view_form_in_gantt`
- Name: event.track.view.form.in.gantt
- Model: `event.track`
- Type: inferred from arch
- Inherits: `website_event_track.view_event_track_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_unschedule`, `unlink`
- XPath or positional patches: 5

## Actions

- `website_event_track.action_event_track_from_event`: `act_window`
- `website_event_track.action_event_track`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_event_track_gantt/Views]]

<!-- GENERATED:VIEWFILE -->
