<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# LivechatController

- Module: [[docs/Community Addons/im_livechat/im_livechat|im_livechat]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 13

## Routes

### `external_lib`
- Paths: `/im_livechat/external_lib.<any(css,js):ext>`
- Type: `http`
- Auth: `public`

### `assets_embed`
- Paths: `/im_livechat/assets_embed.<any(css, js):ext>`
- Type: `http`
- Auth: `public`

### `fontawesome`
- Paths: `/im_livechat/font-awesome`
- Type: `http`
- Auth: `none`

### `odoo_ui_icons`
- Paths: `/im_livechat/odoo_ui_icons`
- Type: `http`
- Auth: `none`

### `get_emoji_bundle`
- Paths: `/im_livechat/emoji_bundle`
- Type: `http`
- Auth: `public`

### `support_page`
- Paths: `/im_livechat/support/<int:channel_id>`
- Type: `http`
- Auth: `public`

### `loader`
- Paths: `/im_livechat/loader/<int:channel_id>`
- Type: `http`
- Auth: `public`

### `get_session`
- Paths: `/im_livechat/get_session`
- Type: `jsonrpc`
- Auth: `public`

### `feedback`
- Paths: `/im_livechat/feedback`
- Type: `jsonrpc`
- Auth: `public`

### `history_pages`
- Paths: `/im_livechat/history`
- Type: `jsonrpc`
- Auth: `public`

### `email_livechat_transcript`
- Paths: `/im_livechat/email_livechat_transcript`
- Type: `jsonrpc`
- Auth: `user`

### `download_livechat_transcript`
- Paths: `/im_livechat/download_transcript/<int:channel_id>`
- Type: `http`
- Auth: `public`

### `visitor_leave_session`
- Paths: `/im_livechat/visitor_leave_session`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/im_livechat/Controllers]]

<!-- GENERATED:CONTROLLER -->
