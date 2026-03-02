<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# SocialFacebookController

- Module: [[docs/Enterprise Addons/social_facebook/social_facebook|social_facebook]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `SocialController`
- Routes: 8

## Routes

### `social_facebook_account_callback`
- Paths: `/social_facebook/callback`
- Type: `http`
- Auth: `user`

### `social_facebook_add_comment`
- Paths: `/social_facebook/comment`
- Type: `http`
- Auth: `user`

### `social_facebook_delete_comment`
- Paths: `/social_facebook/delete_comment`
- Type: `jsonrpc`
- Auth: `user`

### `social_facebook_get_comments`
- Paths: `/social_facebook/get_comments`
- Type: `jsonrpc`
- Auth: `user`

### `social_facebook_like_comment`
- Paths: `/social_facebook/like_comment`
- Type: `jsonrpc`
- Auth: `user`

### `social_facebook_like_post`
- Paths: `/social_facebook/like_post`
- Type: `jsonrpc`
- Auth: `user`

### `social_facebook_deletion_callback`
- Paths: `/social_facebook/deletion_callback`
- Type: `http`
- Auth: `none`

### `social_facebook_redirect_to_profile`
- Paths: `/social_facebook/redirect_to_profile/<int:account_id>/<facebook_user_id>`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_facebook/Controllers]]

<!-- GENERATED:CONTROLLER -->
