<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# RoomController

- Module: [[docs/Enterprise Addons/room/room|room]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 6

## Routes

### `room_book`
- Paths: `/room/<string:short_code>/book`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_existing_bookings`
- Paths: `/room/<string:access_token>/get_existing_bookings`
- Type: `jsonrpc`
- Auth: `public`

### `room_background_image`
- Paths: `/room/<string:access_token>/background`
- Type: `http`
- Auth: `public`

### `room_booking_create`
- Paths: `/room/<string:access_token>/booking/create`
- Type: `jsonrpc`
- Auth: `public`

### `room_booking_delete`
- Paths: `/room/<string:access_token>/booking/<int:booking_id>/delete`
- Type: `jsonrpc`
- Auth: `public`

### `room_booking_update`
- Paths: `/room/<string:access_token>/booking/<int:booking_id>/update`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/room/Controllers]]

<!-- GENERATED:CONTROLLER -->
