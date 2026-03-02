<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 6, `Char` x 1, `Float` x 1, `Integer` x 3, `Selection` x 3
- Relation fields: 0

## Sample fields

- `absence_management`: `Boolean` (related `company_id.absence_management`)
- `attendance_barcode_source`: `Selection` (related `company_id.attendance_barcode_source`)
- `attendance_device_tracking`: `Boolean` (related `company_id.attendance_device_tracking`)
- `attendance_from_systray`: `Boolean` (related `company_id.attendance_from_systray`)
- `attendance_kiosk_delay`: `Integer` (related `company_id.attendance_kiosk_delay`)
- `attendance_kiosk_mode`: `Selection` (related `company_id.attendance_kiosk_mode`)
- `attendance_kiosk_url`: `Char` (related `company_id.attendance_kiosk_url`)
- `attendance_kiosk_use_pin`: `Boolean` (related `company_id.attendance_kiosk_use_pin`)
- `attendance_overtime_validation`: `Selection` (related `company_id.attendance_overtime_validation`)
- `auto_check_out`: `Boolean` (related `company_id.auto_check_out`)
- `auto_check_out_tolerance`: `Float` (related `company_id.auto_check_out_tolerance`)
- `hr_attendance_display_overtime`: `Boolean` (related `company_id.hr_attendance_display_overtime`)
- `overtime_company_threshold`: `Integer`
- `overtime_employee_threshold`: `Integer`

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Models]]

<!-- GENERATED:MODEL -->
