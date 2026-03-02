<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream.post

- Module: [[docs/Enterprise Addons/social_facebook/social_facebook|social_facebook]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_stream_post.py`
- Python classes: `SocialStreamPost`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 2, `Char` x 3, `Integer` x 4
- Relation fields: 0

## Sample fields

- `facebook_author_id`: `Char` (comodel `Facebook Author ID`)
- `facebook_comments_count`: `Integer` (comodel `Comments`)
- `facebook_is_event_post`: `Boolean` (comodel `Is event post`)
- `facebook_likes_count`: `Integer` (comodel `Likes`)
- `facebook_post_id`: `Char` (comodel `Facebook Post ID`)
- `facebook_reach`: `Integer` (comodel `Reach`)
- `facebook_reactions_count`: `Char` (comodel `Reactions Count`)
- `facebook_shares_count`: `Integer` (comodel `Shares`)
- `facebook_user_likes`: `Boolean` (comodel `User Likes`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_author_link`, `_compute_is_author`, `_compute_post_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_facebook/Models]]

<!-- GENERATED:MODEL -->
