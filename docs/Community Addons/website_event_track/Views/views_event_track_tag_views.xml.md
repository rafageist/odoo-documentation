---
tags: [odoo, community, generated, views]
---

# views/event_track_tag_views.xml

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `views/event_track_tag_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_event_track_tag_tree`
- Name: Tracks Tag
- Model: `event.track.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `category_id`, `color`, `name`, `sequence`
- XPath or positional patches: 0

### `view_event_track_tag_form`
- Name: Track Tags
- Model: `event.track.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `category_id`, `color`, `name`
- XPath or positional patches: 0

### `event_track_tag_category_view_list`
- Name: event.track.tag.category.view.list
- Model: `event.track.tag.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

### `event_track_tag_category_view_form`
- Name: event.track.tag.category.view.form
- Model: `event.track.tag.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `color`, `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

## Actions

- `action_event_track_tag`: `act_window` Track Tags
- `event_track_tag_category_action`: `act_window` Track Tag Categories

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Views]]

