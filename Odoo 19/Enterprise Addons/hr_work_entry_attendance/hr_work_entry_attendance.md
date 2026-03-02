
<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Work Entries - Attendance

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/hr_work_entry_attendance
- Dependencies: [[Odoo 19/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]], [[Odoo 19/Community Addons/hr_attendance/hr_attendance|hr_attendance]]

## Summary

Create work entries from the employee's attendances

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrAttendance`
- `hr.attendance.overtime.line`
- `hr.attendance.overtime.rule`
- `hr.attendance.overtime.ruleset`
- `HrEmployee`
- `HrVersion`
- `HrWorkEntry`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Attendance - Models and Relations
class HrAttendance
class "hr.attendance.overtime.line" as hr_attendance_overtime_line
class "hr.attendance.overtime.rule" as hr_attendance_overtime_rule
class "hr.attendance.overtime.ruleset" as hr_attendance_overtime_ruleset
class HrEmployee
class HrVersion
class HrWorkEntry
class "hr.work.entry.type" as hr_work_entry_type
hr_attendance_overtime_line --> hr_work_entry_type : many2one
hr_attendance_overtime_rule --> hr_work_entry_type : many2one
class "hr.attendance" as hr_attendance
HrWorkEntry --> hr_attendance : many2one
HrWorkEntry --> hr_attendance_overtime_line : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
