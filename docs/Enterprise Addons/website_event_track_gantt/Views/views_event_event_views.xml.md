---
tags: [odoo, enterprise, generated, views]
---

# views/event_event_views.xml

- Module: [[docs/Enterprise Addons/website_event_track_gantt/website_event_track_gantt|website_event_track_gantt]]
- Scope: Enterprise Addons
- Source file: `views/event_event_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_event_view_form`
- Name: event.event.view.form.inherit.enterprise
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `track_count`, `track_gantt_initial_date`, `track_gantt_scale`
- Buttons: `%(website_event_track.action_event_track_from_event)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_event_track_gantt/Views]]

