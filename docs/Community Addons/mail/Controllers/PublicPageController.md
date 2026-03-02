<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PublicPageController

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `controllers/discuss/public_page.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `discuss_channel_chat_from_token`
- Paths: `/chat/<string:create_token>`, `/chat/<string:create_token>/<string:channel_name>`
- Type: `http`
- Auth: `public`

### `discuss_channel_meet_from_token`
- Paths: `/meet/<string:create_token>`, `/meet/<string:create_token>/<string:channel_name>`
- Type: `http`
- Auth: `public`

### `discuss_channel_invitation`
- Paths: `/chat/<int:channel_id>/<string:invitation_token>`
- Type: `http`
- Auth: `public`

### `discuss_channel`
- Paths: `/discuss/channel/<int:channel_id>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/mail/Controllers]]

<!-- GENERATED:CONTROLLER -->
