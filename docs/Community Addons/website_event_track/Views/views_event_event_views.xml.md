<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_event_views.xml

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `views/event_event_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_event_view_list`
- Name: event.event.view.list.inherit.website.event.track
- Model: `event.event`
- Type: inferred from arch
- Inherits: `event.view_event_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `stage_id`, `track_count`
- XPath or positional patches: 0

### `event_event_view_form`
- Name: event.event.view.from.inherit.track
- Model: `event.event`
- Type: inferred from arch
- Inherits: `website_event.event_event_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `track_count`, `website_track`, `website_track_proposal`
- Buttons: `%(action_event_track_from_event)d`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Views]]

<!-- GENERATED:VIEWFILE -->
