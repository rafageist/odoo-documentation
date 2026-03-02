<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# RtcController

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `controllers/discuss/rtc.py`
- Base classes: `http.Controller`
- Routes: 8

## Routes

### `session_call_notify`
- Paths: `/mail/rtc/session/notify_call_members`
- Type: `jsonrpc`
- Auth: `public`

### `session_update_and_broadcast`
- Paths: `/mail/rtc/session/update_and_broadcast`
- Type: `jsonrpc`
- Auth: `public`

### `channel_call_join`
- Paths: `/mail/rtc/channel/join_call`
- Type: `jsonrpc`
- Auth: `public`

### `channel_call_leave`
- Paths: `/mail/rtc/channel/leave_call`
- Type: `jsonrpc`
- Auth: `public`

### `channel_upgrade`
- Paths: `/mail/rtc/channel/upgrade_connection`
- Type: `jsonrpc`
- Auth: `user`

### `channel_call_cancel_invitation`
- Paths: `/mail/rtc/channel/cancel_call_invitation`
- Type: `jsonrpc`
- Auth: `public`

### `audio_worklet_processor`
- Paths: `/mail/rtc/audio_worklet_processor_v2`
- Type: `http`
- Auth: `public`
- Readonly: `True`

### `channel_ping`
- Paths: `/discuss/channel/ping`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/mail/Controllers]]

<!-- GENERATED:CONTROLLER -->
