<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream.post

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_stream_post.py`
- Python classes: `SocialStreamPost`

## Field footprint

- Detected fields: 6
- Field types: `Char` x 2, `Integer` x 4
- Relation fields: 0

## Sample fields

- `youtube_comments_count`: `Integer` (comodel `YouTube Comments Count`)
- `youtube_dislikes_count`: `Integer` (comodel `YouTube Dislikes`)
- `youtube_likes_count`: `Integer` (comodel `YouTube Likes`)
- `youtube_thumbnail_url`: `Char` (comodel `YouTube Thumbnail Url`, compute `_compute_youtube_thumbnail_url`)
- `youtube_video_id`: `Char` (comodel `YouTube Video ID`)
- `youtube_views_count`: `Integer` (comodel `YouTube Views`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_author_link`, `_compute_is_author`, `_compute_post_link`, `_compute_youtube_thumbnail_url`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Models]]

<!-- GENERATED:MODEL -->
