<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.company

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 6, `Char` x 2, `Float` x 1, `Integer` x 3, `Selection` x 3
- Relation fields: 0

## Sample fields

- `absence_management`: `Boolean`
- `attendance_barcode_source`: `Selection`
- `attendance_device_tracking`: `Boolean`
- `attendance_from_systray`: `Boolean`
- `attendance_kiosk_delay`: `Integer`
- `attendance_kiosk_key`: `Char`
- `attendance_kiosk_mode`: `Selection`
- `attendance_kiosk_url`: `Char` (compute `_compute_attendance_kiosk_url`)
- `attendance_kiosk_use_pin`: `Boolean`
- `attendance_overtime_validation`: `Selection`
- `auto_check_out`: `Boolean`
- `auto_check_out_tolerance`: `Float`
- `hr_attendance_display_overtime`: `Boolean`
- `overtime_company_threshold`: `Integer`
- `overtime_employee_threshold`: `Integer`

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_attendance_kiosk_url`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Models]]

<!-- GENERATED:MODEL -->
