<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# SocialInstagramController

- Module: [[docs/Enterprise Addons/social_instagram/social_instagram|social_instagram]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `SocialController`
- Routes: 5

## Routes

### `social_instagram_callback`
- Paths: `/social_instagram/callback`
- Type: `http`
- Auth: `user`

### `social_instagram_comment`
- Paths: `/social_instagram/comment`
- Type: `http`
- Auth: `user`

### `social_instagram_delete_comment`
- Paths: `/social_instagram/delete_comment`
- Type: `jsonrpc`
- Auth: `user`

### `social_instagram_get_comments`
- Paths: `/social_instagram/get_comments`
- Type: `jsonrpc`
- Auth: `user`

### `social_post_instagram_image`
- Paths: `/social_instagram/<string:instagram_access_token>/get_image/<int:image_id>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_instagram/Controllers]]

<!-- GENERATED:CONTROLLER -->
