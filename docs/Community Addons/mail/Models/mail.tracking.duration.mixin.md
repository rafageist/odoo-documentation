<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.tracking.duration.mixin

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mail_tracking_duration_mixin.py`
- Python classes: `MailTrackingDurationMixin`
- Description: Mixin to compute the time a record has spent in each value a many2one field can take
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Integer` x 1, `Json` x 1
- Relation fields: 0

## Sample fields

- `duration_tracking`: `Json` (compute `_compute_duration_tracking`)
- `is_rotting`: `Boolean` (comodel `Rotting`, compute `_compute_rotting`)
- `rotting_days`: `Integer` (comodel `Days Rotting`, compute `_compute_rotting`)

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_duration_tracking`, `_compute_rotting`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mail/Models]]

<!-- GENERATED:MODEL -->
