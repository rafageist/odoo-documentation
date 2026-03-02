<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.hr.attendance
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `absence_management`, `attendance_barcode_source`, `attendance_device_tracking`, `attendance_from_systray`, `attendance_kiosk_delay`, `attendance_kiosk_mode`, `attendance_kiosk_url`, `attendance_kiosk_use_pin`, `attendance_overtime_validation`, `auto_check_out`, and 4 more
- Buttons: `regenerate_kiosk_key`
- XPath or positional patches: 1

## Actions

- `action_hr_attendance_settings`: `act_window` Settings

## Menus

- `menu_hr_attendance_settings`: Settings

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
