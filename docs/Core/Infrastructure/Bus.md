---
tags: [core, infrastructure, bus]
status: active
---

# Bus/Events

## Focus
- `bus.bus` notifications, channel subscriptions, and longpolling entry points.
- Event propagation between backend writes and client refreshes.
- Shared patterns reused by mail, barcode, POS, and collaborative UI features.

## Odoo 19 runtime model
- The modern live-refresh path is websocket-centered. `addons/bus/controllers/websocket.py` exposes `/websocket` for the handshake and `/websocket/peek_notifications` for compatibility/session probing.
- The frontend `bus_service` prefers a `SharedWorker` so multiple tabs can share one live connection; it falls back to a normal `Worker` when shared workers are unavailable.
- `bus.models.ir_http` extends both backend and frontend session payloads with `websocket_worker_version`, which is how the client knows which worker bundle and websocket version to request.
- `ir.websocket` authenticates the websocket request, expands the effective channel list, and bridges the transport to `bus.bus._poll(...)`.

## Channel model
- The raw client-supplied channel list is not the whole subscription surface.
- `ir.websocket._build_bus_channel_list(...)` always adds `broadcast`, all current user groups, and the current partner when a real session exists.
- That means many refreshes are implicitly keyed off user identity and group membership even if the browser only asked for a small set of business channels.

## Operational behavior
- The worker tracks the last notification id so it can request missed notifications without duplicating ones already seen by the tab set.
- Network transitions are first-class: `bus_service` pauses on `offline`, delays reconnect on `online`, and warns the UI when the worker becomes outdated.
- A stale or broken live UI can come from worker initialization, websocket handshake, channel subscription drift, or server-side notification dispatch. It is not automatically an ORM cache issue.

## Related notes
- `[[docs/Core/Framework/Runtime Lifecycle]]`
- `[[docs/Core/Framework/http]]`

## Navigation
- **Parent:** [[docs/Core/Infrastructure/Infrastructure]]
