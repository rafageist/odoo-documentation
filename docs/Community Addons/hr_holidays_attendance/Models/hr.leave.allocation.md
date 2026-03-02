<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.allocation

- Module: [[docs/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_leave_allocation.py`
- Python classes: `HrLeaveAllocation`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Float` x 1
- Relation fields: 0

## Sample fields

- `employee_overtime`: `Float` (related `employee_id.total_overtime`)
- `overtime_deductible`: `Boolean` (compute `_compute_overtime_deductible`)

## Method hints

- Detected methods: 6
- Action methods: `action_refuse`
- Compute methods: `_compute_overtime_deductible`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays_attendance/Models]]

<!-- GENERATED:MODEL -->
