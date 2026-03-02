<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.track

- Module: [[docs/Community Addons/website_event_track_live/website_event_track_live|website_event_track_live]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/event_track.py`
- Python classes: `EventTrack`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 2, `Char` x 2
- Relation fields: 0

## Sample fields

- `is_youtube_chat_available`: `Boolean` (comodel `Is Chat Available`, compute `_compute_is_youtube_chat_available`)
- `is_youtube_replay`: `Boolean` (comodel `Is YouTube Replay`)
- `youtube_video_id`: `Char` (comodel `YouTube video ID`, compute `_compute_youtube_video_id`)
- `youtube_video_url`: `Char` (comodel `YouTube Video Link`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_is_youtube_chat_available`, `_compute_website_image_url`, `_compute_youtube_video_id`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track_live/Models]]

<!-- GENERATED:MODEL -->
