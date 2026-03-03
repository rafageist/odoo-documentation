---
tags: [odoo, enterprise, generated, views]
---

# views/room_room_views.xml

- Module: [[docs/Enterprise Addons/room/room|room]]
- Scope: Enterprise Addons
- Source file: `views/room_room_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `room_room_view_form`
- Name: room.room.view.form
- Model: `room.room`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `active`, `bookable_background_color`, `booked_background_color`, `description`, `is_available`, `name`, `next_booking_start`, `office_id`, `room_background_image`, `room_booking_ids`, and 3 more
- Buttons: `action_open_booking_view`, `action_view_bookings`
- XPath or positional patches: 0

### `room_room_view_list`
- Name: room.room.view.list
- Model: `room.room`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `is_available`, `name`, `next_booking_start`, `office_id`, `room_properties`
- XPath or positional patches: 0

### `room_room_view_kanban`
- Name: room.room.view.kanban
- Model: `room.room`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `active`, `is_available`, `name`, `next_booking_start`, `office_id`, `room_background_image`, `room_properties`
- XPath or positional patches: 0

### `room_room_view_search`
- Name: Room search view
- Model: `room.room`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `name`, `office_id`, `room_properties`
- XPath or positional patches: 0

## Actions

- `room_room_action`: `act_window` Room

## Navigation

- **Parent:** [[docs/Enterprise Addons/room/Views]]

