<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream.post

- Module: [[docs/Enterprise Addons/social_instagram/social_instagram|social_instagram]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_stream_post.py`
- Python classes: `SocialStreamPost`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 3, `Integer` x 2
- Relation fields: 0

## Sample fields

- `instagram_comments_count`: `Integer` (comodel `Instagram Comments`)
- `instagram_comments_disabled`: `Boolean` (comodel `Instagram Comments Disabled`)
- `instagram_facebook_author_id`: `Char` (comodel `Instagram Facebook Author ID`)
- `instagram_likes_count`: `Integer` (comodel `Instagram Likes`)
- `instagram_post_id`: `Char` (comodel `Instagram Post ID`)
- `instagram_post_link`: `Char` (comodel `Instagram Post URL`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_author_link`, `_compute_is_author`, `_compute_post_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_instagram/Models]]

<!-- GENERATED:MODEL -->
