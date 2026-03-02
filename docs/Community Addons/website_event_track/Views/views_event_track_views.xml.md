<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_track_views.xml

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `views/event_track_views.xml`
- Views: 7
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `view_event_track_graph`
- Name: event.track.graph
- Model: `event.track`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `color`, `duration`, `location_id`, `website_cta_delay`
- XPath or positional patches: 0

### `view_event_track_tree`
- Name: event.track.list
- Model: `event.track`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `active`, `activity_exception_decoration`, `color`, `event_id`, `location_id`, `name`, `partner_email`, `partner_id`, `partner_name`, `partner_phone`, and 3 more
- XPath or positional patches: 0

### `view_event_track_form`
- Name: event.track.form
- Model: `event.track`
- Type: inferred from arch
- Root tag: `form`
- Field references: 35
- Sample fields: `active`, `color`, `company_id`, `contact_email`, `contact_phone`, `date`, `description`, `duration`, `event_id`, `image`, and 25 more
- Buttons: `%(website_event_track.website_visitor_action_from_track)d`
- XPath or positional patches: 0

### `view_event_track_search`
- Name: event.track.search
- Model: `event.track`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `event_id`, `location_id`, `name`, `partner_id`, `stage_id`, `tag_ids`
- XPath or positional patches: 0

### `view_event_track_calendar`
- Name: event.track.calendar
- Model: `event.track`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `event_id`, `location_id`, `partner_id`, `user_id`
- XPath or positional patches: 0

### `view_event_track_kanban`
- Name: event.track.kanban
- Model: `event.track`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `activity_ids`, `color`, `duration`, `kanban_state`, `legend_blocked`, `legend_done`, `legend_normal`, `name`, `partner_id`, `priority`, and 2 more
- XPath or positional patches: 0

### `event_track_view_form_quick_create`
- Name: event.track.view.form.quick.create
- Model: `event.track`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `date`, `event_id`, `name`
- XPath or positional patches: 0

## Actions

- `event_track_action_from_visitor`: `act_window` Wishlisted Tracks
- `action_event_track_from_event`: `act_window` Event Tracks
- `action_event_track`: `act_window` Event Tracks
- `website_visitor_action_from_track`: `act_window` Visitors Wishlist

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Views]]

<!-- GENERATED:VIEWFILE -->
