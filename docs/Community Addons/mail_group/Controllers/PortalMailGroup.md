<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# PortalMailGroup

- Module: [[docs/Community Addons/mail_group/mail_group|mail_group]]
- Scope: Community Addons
- Source file: `controllers/portal.py`
- Base classes: `http.Controller`
- Routes: 9

## Routes

### `groups_index`
- Paths: `/groups`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `group_view_messages`
- Paths: `/groups/<model("mail.group"):group>`, `/groups/<model("mail.group"):group>/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `group_view_message`
- Paths: `/groups/<model("mail.group"):group>/<model("mail.group.message"):message>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `group_message_get_replies`
- Paths: `/groups/<model("mail.group"):group>/<model("mail.group.message"):message>/get_replies`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `group_unsubscribe_oneclick`
- Paths: `/group/<int:group_id>/unsubscribe_oneclick`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `group_subscribe`
- Paths: `/group/subscribe`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `group_unsubscribe`
- Paths: `/group/unsubscribe`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `group_subscribe_confirm`
- Paths: `/group/subscribe-confirm`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `group_unsubscribe_confirm`
- Paths: `/group/unsubscribe-confirm`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/mail_group/Controllers]]

<!-- GENERATED:CONTROLLER -->
