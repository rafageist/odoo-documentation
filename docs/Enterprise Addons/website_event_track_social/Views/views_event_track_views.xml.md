---
tags: [odoo, enterprise, generated, views]
---

# views/event_track_views.xml

- Module: [[docs/Enterprise Addons/website_event_track_social/website_event_track_social|website_event_track_social]]
- Scope: Enterprise Addons
- Source file: `views/event_track_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_track_view_graph`
- Name: event.track.view.graph.inherit.social
- Model: `event.track`
- Type: inferred from arch
- Inherits: `website_event_track.view_event_track_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `push_reminder_delay`
- XPath or positional patches: 1

### `event_track_view_form`
- Name: event.track.view.form.inherit.social
- Model: `event.track`
- Type: inferred from arch
- Inherits: `website_event_track.view_event_track_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `firebase_enable_push_notifications`, `push_reminder`, `push_reminder_delay`, `push_reminder_posts`
- Buttons: `action_edit_reminder`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_event_track_social/Views]]

