<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.stream.post

- Module: [[docs/Enterprise Addons/social_linkedin/social_linkedin|social_linkedin]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_stream_post.py`
- Python classes: `SocialStreamPost`

## Field footprint

- Detected fields: 7
- Field types: `Char` x 5, `Integer` x 2
- Relation fields: 0

## Sample fields

- `linkedin_author_id`: `Char` (comodel `LinkedIn author ID`, compute `_compute_linkedin_author_urn`)
- `linkedin_author_image_url`: `Char` (comodel `LinkedIn author image URL`)
- `linkedin_author_urn`: `Char` (comodel `LinkedIn author URN`)
- `linkedin_author_vanity_name`: `Char` (comodel `LinkedIn Vanity Name`)
- `linkedin_comments_count`: `Integer` (comodel `LinkedIn Comments`)
- `linkedin_likes_count`: `Integer` (comodel `LinkedIn Likes`)
- `linkedin_post_urn`: `Char` (comodel `LinkedIn post URN`)

## Method hints

- Detected methods: 14
- Action methods: none
- Compute methods: `_compute_author_link`, `_compute_is_author`, `_compute_linkedin_author_urn`, `_compute_post_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_linkedin/Models]]

<!-- GENERATED:MODEL -->
