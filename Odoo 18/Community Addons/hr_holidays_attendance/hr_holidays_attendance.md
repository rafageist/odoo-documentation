<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# HR Attendance Holidays

- Version: v18
- Category: community
- Source: odoo/addons/hr_holidays_attendance
- Dependencies: [[Odoo 18/Community Addons/hr_attendance/hr_attendance|hr_attendance]], [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Attendance Holidays

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrAttendance`
- `HRLeave`
- `AccrualPlanLevel`
- `HolidaysAllocation`
- `HRLeaveType`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title HR Attendance Holidays - Models and Relations
class HrAttendance
class HRLeave
class AccrualPlanLevel
class HolidaysAllocation
class HRLeaveType
class ResUsers
class "hr.attendance.overtime" as hr_attendance_overtime
HRLeave --> hr_attendance_overtime : many2one
HolidaysAllocation --> hr_attendance_overtime : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
