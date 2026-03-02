<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsocketController

- Module: [[docs/Community Addons/bus/bus|bus]]
- Scope: Community Addons
- Source file: `controllers/websocket.py`
- Base classes: `Controller`
- Routes: 5

## Routes

### `websocket`
- Paths: `/websocket`
- Type: `http`
- Auth: `public`

### `health`
- Paths: `/websocket/health`
- Type: `http`
- Auth: `none`

### `peek_notifications`
- Paths: `/websocket/peek_notifications`
- Type: `jsonrpc`
- Auth: `public`

### `on_websocket_closed`
- Paths: `/websocket/on_closed`
- Type: `jsonrpc`
- Auth: `public`

### `get_websocket_worker_bundle`
- Paths: `/bus/websocket_worker_bundle`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/bus/Controllers]]

<!-- GENERATED:CONTROLLER -->
