<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.post

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_post.py`
- Python classes: `SocialPost`

## Field footprint

- Detected fields: 12
- Field types: `Char` x 7, `Html` x 1, `Integer` x 2, `Selection` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `youtube_access_token`: `Char` (comodel `YouTube Access Token`, compute `_compute_youtube_access_token`)
- `youtube_accounts_count`: `Integer` (comodel `Selected YouTube Accounts`, compute `_compute_youtube_accounts_count`)
- `youtube_accounts_other_count`: `Integer` (comodel `Selected Other Accounts`, compute `_compute_youtube_accounts_count`)
- `youtube_description`: `Text` (comodel `YouTube Video Description`)
- `youtube_preview`: `Html` (comodel `YouTube Preview`, compute `_compute_youtube_preview`)
- `youtube_thumbnail_url`: `Char` (comodel `YouTube Thumbnail Url`, compute `_compute_youtube_thumbnail_url`)
- `youtube_title`: `Char` (comodel `YouTube Video Title`)
- `youtube_video`: `Char` (comodel `YouTube Video`)
- `youtube_video_category_id`: `Char` (comodel `YouTube Category Id`)
- `youtube_video_id`: `Char` (comodel `YouTube Video Id`)
- `youtube_video_privacy`: `Selection`
- `youtube_video_url`: `Char` (comodel `YouTube Video Url`, compute `_compute_youtube_video_url`)

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_stream_posts_count`, `_compute_youtube_access_token`, `_compute_youtube_accounts_count`, `_compute_youtube_preview`, `_compute_youtube_thumbnail_url`, `_compute_youtube_video_url`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Models]]

<!-- GENERATED:MODEL -->
