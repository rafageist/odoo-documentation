<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.employee

- Module: [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `has_work_entries`: `Boolean` (compute `_compute_has_work_entries`)
- `work_entry_source`: `Selection` (related `version_id.work_entry_source`)
- `work_entry_source_calendar_invalid`: `Boolean` (related `version_id.work_entry_source_calendar_invalid`)

## Method hints

- Detected methods: 3
- Action methods: `action_open_work_entries`
- Compute methods: `_compute_has_work_entries`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/hr_work_entry/Models]]

<!-- GENERATED:MODEL -->
