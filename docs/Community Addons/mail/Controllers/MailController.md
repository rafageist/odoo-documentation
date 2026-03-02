<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# MailController

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `controllers/mail.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `mail_action_view`
- Paths: `/mail/view`
- Type: `http`
- Auth: `public`

### `mail_action_unfollow`
- Paths: `/mail/unfollow`
- Type: `http`
- Auth: `public`

### `mail_thread_message_redirect`
- Paths: `/mail/message/<int:message_id>`
- Type: `http`
- Auth: `public`

### `export_icon_to_png`
- Paths: `/mail/font_to_img/<icon>`, `/mail/font_to_img/<icon>/<color>`, `/mail/font_to_img/<icon>/<color>/<bg>`, `/mail/font_to_img/<icon>/<color>/<bg>/<int:size>`, `/mail/font_to_img/<icon>/<color>/<bg>/<int:width>x<int:height>`, `/mail/font_to_img/<icon>/<color>/<bg>/<int:width>x<int:height>/<int:alpha>`, `/mail/font_to_img/<icon>/<color>/<int:size>`, `/mail/font_to_img/<icon>/<color>/<int:size>/<int:alpha>`, `/mail/font_to_img/<icon>/<color>/<int:width>x<int:height>`, `/mail/font_to_img/<icon>/<color>/<int:width>x<int:height>/<int:alpha>`, and 10 more
- Type: `http`
- Auth: `none`

## Navigation

- **Parent:** [[docs/Community Addons/mail/Controllers]]

<!-- GENERATED:CONTROLLER -->
