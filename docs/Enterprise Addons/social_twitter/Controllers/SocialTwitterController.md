<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# SocialTwitterController

- Module: [[docs/Enterprise Addons/social_twitter/social_twitter|social_twitter]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `SocialController`
- Routes: 8

## Routes

### `social_twitter_account_callback`
- Paths: `/social_twitter/callback`
- Type: `http`
- Auth: `user`

### `social_twitter_comment`
- Paths: `/social_twitter/<int:stream_id>/comment`
- Type: `http`

### `social_twitter_delete_tweet`
- Paths: `/social_twitter/delete_tweet`
- Type: `jsonrpc`

### `social_twitter_get_comments`
- Paths: `/social_twitter/get_comments`
- Type: `jsonrpc`

### `social_twitter_like_tweet`
- Paths: `/social_twitter/<int:stream_id>/like_tweet`
- Type: `jsonrpc`

### `social_twitter_do_retweet`
- Paths: `/social_twitter/<int:stream_id>/retweet`
- Type: `jsonrpc`
- Auth: `user`

### `social_twitter_undo_retweet`
- Paths: `/social_twitter/<int:stream_id>/unretweet`
- Type: `jsonrpc`
- Auth: `user`

### `social_twitter_tweet_quote`
- Paths: `/social_twitter/<int:stream_id>/quote`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_twitter/Controllers]]

<!-- GENERATED:CONTROLLER -->
