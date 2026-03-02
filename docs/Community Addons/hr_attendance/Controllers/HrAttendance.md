<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# HrAttendance

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 13

## Routes

### `kiosk_menu_item_action`
- Paths: `/hr_attendance/kiosk_mode_menu/<int:company_id>`
- Type: `http`
- Auth: `user`

### `get_employees_without_badge`
- Paths: `/hr_attendance/get_employees_without_badge`
- Type: `jsonrpc`
- Auth: `public`

### `set_badge`
- Paths: `/hr_attendance/set_badge`
- Type: `jsonrpc`
- Auth: `public`

### `create_employee`
- Paths: `/hr_attendance/create_employee`
- Type: `jsonrpc`
- Auth: `public`

### `kiosk_keepalive`
- Paths: `/hr_attendance/kiosk_keepalive`
- Type: `jsonrpc`
- Auth: `user`

### `open_kiosk_mode`
- Paths: `/hr_attendance/<token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `employee_attendance_data`
- Paths: `/hr_attendance/attendance_employee_data`
- Type: `jsonrpc`
- Auth: `public`

### `scan_barcode`
- Paths: `/hr_attendance/attendance_barcode_scanned`
- Type: `jsonrpc`
- Auth: `public`

### `manual_selection`
- Paths: `/hr_attendance/manual_selection`
- Type: `jsonrpc`
- Auth: `public`

### `employees_infos`
- Paths: `/hr_attendance/employees_infos`
- Type: `jsonrpc`
- Auth: `public`

### `systray_attendance`
- Paths: `/hr_attendance/systray_check_in_out`
- Type: `jsonrpc`
- Auth: `user`

### `user_attendance_data`
- Paths: `/hr_attendance/attendance_user_data`
- Type: `jsonrpc`
- Auth: `user`
- Readonly: `True`

### `set_attendance_settings`
- Paths: `/hr_attendance/set_settings`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Controllers]]

<!-- GENERATED:CONTROLLER -->
