<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# calendar.event

- Module: [[docs/Enterprise Addons/pos_appointment/pos_appointment|pos_appointment]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/calendar_event.py`
- Python classes: `CalendarEvent`
- Inherits: `pos.load.mixin`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 2, `Integer` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `answers`: `Char` (comodel `Q&A answers`, compute `_compute_answers`)
- `appointment_status`: `Selection`
- `phone_number`: `Char`
- `waiting_list_capacity`: `Integer` (compute `_compute_waiting_list_capacity`, store `True`)

## Method hints

- Detected methods: 11
- Action methods: `action_create_booking_form_view`, `action_open_booking_form_view`, `action_open_booking_gantt_view`
- Compute methods: `_compute_answers`, `_compute_waiting_list_capacity`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_appointment/Models]]

<!-- GENERATED:MODEL -->
