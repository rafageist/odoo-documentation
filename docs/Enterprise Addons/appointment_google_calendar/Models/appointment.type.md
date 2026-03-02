<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# appointment.type

- Module: [[docs/Enterprise Addons/appointment_google_calendar/appointment_google_calendar|appointment_google_calendar]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/appointment_type.py`
- Python classes: `AppointmentType`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Html` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `connector_google`: `Boolean` (compute `_compute_connector_google`)
- `event_videocall_source`: `Selection`
- `users_wo_google_calendar_msg`: `Html` (comodel `Users Without Google Calendar Synchronization`, compute `_compute_users_wo_google_calendar_msg`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_connector_google`, `_compute_users_wo_google_calendar_msg`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment_google_calendar/Models]]

<!-- GENERATED:MODEL -->
