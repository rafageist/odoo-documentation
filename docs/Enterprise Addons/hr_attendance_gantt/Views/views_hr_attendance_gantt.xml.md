<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_attendance_gantt.xml

- Module: [[docs/Enterprise Addons/hr_attendance_gantt/hr_attendance_gantt|hr_attendance_gantt]]
- Scope: Enterprise Addons
- Source file: `views/hr_attendance_gantt.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_attendance_gantt_view`
- Name: hr.attendance.gantt
- Model: `hr.attendance`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 0

### `hr_attendance_gantt_create_view_form`
- Name: hr.attendance.form
- Model: `hr.attendance`
- Type: inferred from arch
- Inherits: `hr_attendance.hr_attendance_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `unlink`
- XPath or positional patches: 6

## Actions

- `hr_attendance.hr_attendance_action`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_attendance_gantt/Views]]

<!-- GENERATED:VIEWFILE -->
