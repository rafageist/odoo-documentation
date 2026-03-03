---
tags: [odoo, enterprise, generated, views]
---

# views/room_booking_views.xml

- Module: [[docs/Enterprise Addons/room/room|room]]
- Scope: Enterprise Addons
- Source file: `views/room_booking_views.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `room_booking_view_form`
- Name: room.booking.view.form
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `name`, `organizer_id`, `room_id`, `start_datetime`, `stop_datetime`
- XPath or positional patches: 0

### `room_booking_view_kanban`
- Name: room.booking.view.kanban
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `display_name`, `organizer_id`, `room_id`, `start_datetime`, `stop_datetime`
- XPath or positional patches: 0

### `room_booking_view_list`
- Name: room.booking.view.list
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `name`, `organizer_id`, `room_id`, `start_datetime`, `stop_datetime`
- XPath or positional patches: 0

### `room_booking_view_calendar`
- Name: room.booking.view.calendar
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `room_id`
- XPath or positional patches: 0

### `room_booking_view_gantt`
- Name: room.booking.view.gantt
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 0

### `room_booking_view_search`
- Name: Bookings search view
- Model: `room.booking`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `office_id`, `organizer_id`, `room_id`
- XPath or positional patches: 0

## Actions

- `room_booking_action`: `act_window` Bookings

## Navigation

- **Parent:** [[docs/Enterprise Addons/room/Views]]

