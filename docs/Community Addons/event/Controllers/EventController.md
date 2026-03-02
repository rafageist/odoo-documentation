<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# EventController

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `Controller`
- Routes: 3

## Routes

### `event_ics_file`
- Paths: `/event/<model("event.event"):event>/ics`
- Type: `http`
- Auth: `public`

### `event_my_tickets`
- Paths: `/event/<int:event_id>/my_tickets`
- Type: `http`
- Auth: `public`

### `init_barcode_interface`
- Paths: `/event/init_barcode_interface`
- Type: `jsonrpc`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/event/Controllers]]

<!-- GENERATED:CONTROLLER -->
