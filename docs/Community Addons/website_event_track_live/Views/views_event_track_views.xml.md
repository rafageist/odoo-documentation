---
tags: [odoo, community, generated, views]
---

# views/event_track_views.xml

- Module: [[docs/Community Addons/website_event_track_live/website_event_track_live|website_event_track_live]]
- Scope: Community Addons
- Source file: `views/event_track_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_track_view_list`
- Name: event.track.view.list.inherit.live
- Model: `event.track`
- Type: inferred from arch
- Inherits: `website_event_track.view_event_track_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `youtube_video_url`
- XPath or positional patches: 1

### `event_track_view_form`
- Name: event.track.view.form.inherit.live
- Model: `event.track`
- Type: inferred from arch
- Inherits: `website_event_track.view_event_track_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `is_youtube_replay`, `youtube_video_url`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track_live/Views]]

