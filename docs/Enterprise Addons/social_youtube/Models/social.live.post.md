<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.live.post

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_live_post.py`
- Python classes: `SocialLivePost`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 2, `Selection` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `youtube_description`: `Text` (related `post_id.youtube_description`)
- `youtube_title`: `Char` (related `post_id.youtube_title`)
- `youtube_video_id`: `Char` (related `post_id.youtube_video_id`)
- `youtube_video_privacy`: `Selection` (related `post_id.youtube_video_privacy`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_live_post_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Models]]

<!-- GENERATED:MODEL -->
