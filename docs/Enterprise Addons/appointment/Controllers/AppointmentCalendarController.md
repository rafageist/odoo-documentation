<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# AppointmentCalendarController

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `controllers/calendar.py`
- Base classes: `CalendarController`
- Routes: 6

## Routes

### `view_meeting`
- Paths: `<dynamic>`

### `appointment_view`
- Paths: `/calendar/view/<string:access_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_add_attendee`
- Paths: `/calendar/<string:access_token>/add_attendees_from_emails`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `appointment_cancel`
- Paths: `/calendar/<string:access_token>/cancel`, `/calendar/cancel/<string:access_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `appointment_get_ics_file`
- Paths: `/calendar/ics/<string:access_token>.ics`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `calendar_videocall`
- Paths: `/calendar/videocall/<string:access_token>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Controllers]]

<!-- GENERATED:CONTROLLER -->
