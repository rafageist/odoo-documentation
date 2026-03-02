<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# EventTrackController

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `controllers/event_track.py`
- Base classes: `http.Controller`
- Routes: 9

## Routes

### `event_tracks`
- Paths: `/event/<model("event.event"):event>/track`, `/event/<model("event.event"):event>/track/tag/<model("event.track.tag"):tag>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `event_agenda`
- Paths: `/event/<model("event.event"):event>/agenda`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_track_page`
- Paths: `/event/<model("event.event", "[('website_track', '=', True)]"):event>/track/<model("event.track", "[('event_id', '=', event.id)]"):track>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `track_reminder_toggle`
- Paths: `/event/track/toggle_reminder`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `send_email_reminder`
- Paths: `/event/track/send_email_reminder`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `event_track_proposal`
- Paths: `/event/<model("event.event"):event>/track_proposal`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `event_track_proposal_post`
- Paths: `/event/<model("event.event"):event>/track_proposal/post`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `website_event_track_fetch_tags`
- Paths: `/event/track_tag/search_read`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `event_track_ics_file`
- Paths: `/event/<model("event.event"):event>/track/<model("event.track"):track>/ics`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Controllers]]

<!-- GENERATED:CONTROLLER -->
