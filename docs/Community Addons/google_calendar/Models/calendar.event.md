<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# calendar.event

- Module: [[docs/Community Addons/google_calendar/google_calendar|google_calendar]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/calendar.py`
- Python classes: `CalendarEvent`
- Inherits: `google.calendar.sync`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `google_id`: `Char` (comodel `Google Calendar Event Id`, compute `_compute_google_id`, store `True`)
- `guests_readonly`: `Boolean` (comodel `Guests Event Modification Permission`)
- `videocall_source`: `Selection`

## Method hints

- Detected methods: 21
- Action methods: `action_mass_archive`
- Compute methods: `_compute_google_id`, `_compute_videocall_source`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/google_calendar/Models]]

<!-- GENERATED:MODEL -->
