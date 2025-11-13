<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Work Entries

- Version: v18
- Category: community
- Source: odoo/addons/hr_work_entry
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]]

## Summary

Manage work entries

## XML Artifacts (detected)

- Views: 15
- Actions: 3
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 5

## Detected Models

- `HrEmployee`
- `hr.work.entry`
- `hr.work.entry.type`
- `hr.user.work.entry.employee`
- `ResourceCalendarAttendance`
- `ResourceCalendarLeave`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Models and Relations
class HrEmployee
class "hr.work.entry" as hr_work_entry
class "hr.work.entry.type" as hr_work_entry_type
class "hr.user.work.entry.employee" as hr_user_work_entry_employee
class ResourceCalendarAttendance
class ResourceCalendarLeave
class "hr.employee" as hr_employee
hr_work_entry --> hr_employee : many2one
hr_work_entry --> hr_work_entry_type : many2one
class "res.company" as res_company
hr_work_entry --> res_company : many2one
class "hr.department" as hr_department
hr_work_entry --> hr_department : many2one
class "res.country" as res_country
hr_work_entry --> res_country : many2one
hr_work_entry_type --> res_country : many2one
class "res.users" as res_users
hr_user_work_entry_employee --> res_users : many2one
hr_user_work_entry_employee --> hr_employee : many2one
ResourceCalendarAttendance --> hr_work_entry_type : many2one
ResourceCalendarLeave --> hr_work_entry_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
