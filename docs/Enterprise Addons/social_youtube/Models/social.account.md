<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# social.account

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/social_account.py`
- Python classes: `SocialAccount`

## Field footprint

- Detected fields: 5
- Field types: `Char` x 4, `Datetime` x 1
- Relation fields: 0

## Sample fields

- `youtube_access_token`: `Char` (comodel `Google Access Token`)
- `youtube_channel_id`: `Char` (comodel `YouTube Channel ID`)
- `youtube_refresh_token`: `Char` (comodel `Google Refresh Token`)
- `youtube_token_expiration_date`: `Datetime` (comodel `Token expiration date`)
- `youtube_upload_playlist_id`: `Char` (comodel `YouTube Upload Playlist ID`)

## Method hints

- Detected methods: 5
- Action methods: `action_youtube_revoke`
- Compute methods: `_compute_stats_link`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Models]]

<!-- GENERATED:MODEL -->
