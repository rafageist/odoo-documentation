<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Attendances

- Version: v18
- Category: community
- Source: odoo/addons/hr_attendance
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/barcodes/barcodes|barcodes]]

## Summary

Track employee attendance

## XML Artifacts (detected)

- Views: 20
- Actions: 11
- Menus: 6
- Rules (ir.rule): 8
- Access CSV entries: 6

## Detected Models

- `hr.attendance`
- `hr.attendance.overtime`
- `HrEmployee`
- `HrEmployeePublic`
- `ResCompany`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Attendances - Models and Relations
class "hr.attendance" as hr_attendance
class "hr.attendance.overtime" as hr_attendance_overtime
class HrEmployee
class HrEmployeePublic
class ResCompany
class User
class "hr.employee" as hr_employee
hr_attendance --> hr_employee : many2one
class "hr.department" as hr_department
hr_attendance --> hr_department : many2one
hr_attendance --> hr_employee : many2one
hr_attendance_overtime --> hr_employee : many2one
class "res.users" as res_users
HrEmployee --> res_users : many2one
HrEmployee --|> hr_attendance : one2many
HrEmployee --> hr_attendance : many2one
HrEmployee --|> hr_attendance_overtime : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
