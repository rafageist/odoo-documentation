<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.version

- Module: [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_version.py`
- Python classes: `HrVersion`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Date` x 1, `Datetime` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `date_generated_from`: `Datetime`
- `date_generated_to`: `Datetime`
- `last_generation_date`: `Date`
- `work_entry_source`: `Selection`
- `work_entry_source_calendar_invalid`: `Boolean` (compute `_compute_work_entry_source_calendar_invalid`)

## Method hints

- Detected methods: 32
- Action methods: none
- Compute methods: `_compute_work_entry_source_calendar_invalid`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/hr_work_entry/Models]]

<!-- GENERATED:MODEL -->
