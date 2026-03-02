<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CalendarController

- Module: [[docs/Community Addons/calendar/calendar|calendar]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 10

## Routes

### `accept_meeting`
- Paths: `/calendar/meeting/accept`
- Type: `http`
- Auth: `calendar`

### `accept_recurrence`
- Paths: `/calendar/recurrence/accept`
- Type: `http`
- Auth: `calendar`

### `decline_meeting`
- Paths: `/calendar/meeting/decline`
- Type: `http`
- Auth: `calendar`

### `decline_recurrence`
- Paths: `/calendar/recurrence/decline`
- Type: `http`
- Auth: `calendar`

### `view_meeting`
- Paths: `/calendar/meeting/view`
- Type: `http`
- Auth: `calendar`

### `calendar_join_meeting`
- Paths: `/calendar/meeting/join`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `notify`
- Paths: `/calendar/notify`
- Type: `jsonrpc`
- Auth: `user`

### `notify_ack`
- Paths: `/calendar/notify_ack`
- Type: `jsonrpc`
- Auth: `user`

### `calendar_join_videocall`
- Paths: `/calendar/join_videocall/<string:access_token>`
- Type: `http`
- Auth: `public`

### `check_calendar_credentials`
- Paths: `/calendar/check_credentials`
- Type: `jsonrpc`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/calendar/Controllers]]

<!-- GENERATED:CONTROLLER -->
