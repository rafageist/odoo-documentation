<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CorsLivechatController

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `controllers/cors/main.py`
- Base classes: `LivechatController`
- Routes: 6

## Routes

### `cors_visitor_leave_session`
- Paths: `/im_livechat/cors/visitor_leave_session`
- Type: `jsonrpc`
- Auth: `public`

### `cors_feedback`
- Paths: `/im_livechat/cors/feedback`
- Type: `jsonrpc`
- Auth: `public`

### `cors_history_pages`
- Paths: `/im_livechat/cors/history`
- Type: `jsonrpc`
- Auth: `public`

### `cors_download_livechat_transcript`
- Paths: `/im_livechat/cors/download_transcript/<int:channel_id>`
- Type: `http`
- Auth: `public`

### `cors_get_session`
- Paths: `/im_livechat/cors/get_session`
- Type: `jsonrpc`
- Auth: `public`

### `cors_livechat_init`
- Paths: `/im_livechat/cors/init`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Controllers]]

<!-- GENERATED:CONTROLLER -->
