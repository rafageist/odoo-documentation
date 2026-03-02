<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_attendance_overtime_views.xml

- Module: [[docs/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- Scope: Community Addons
- Source file: `views/hr_attendance_overtime_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_attendance_overtime_rule_view_form`
- Name: hr.attendance.overtime.rule.form.inherit.hr_work_entry_attendance
- Model: `hr.attendance.overtime.rule`
- Type: inferred from arch
- Inherits: `hr_attendance.hr_attendance_overtime_rule_view_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `compensable_as_leave`
- XPath or positional patches: 1

### `view_attendance_overtime_line_list`
- Name: hr.attendance
- Model: `hr.attendance`
- Type: inferred from arch
- Inherits: `hr_attendance.hr_attendance_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `compensable_as_leave`, `manual_duration`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
