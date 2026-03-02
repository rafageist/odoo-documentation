<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Work Entries

- Scope: Community Addons
- Source: odoo/addons/hr_work_entry
- Dependencies: [[docs/Community Addons/hr/hr|hr]]

## Summary

Manage work entries

## XML Artifacts (detected)

- Views: 19
- Actions: 4
- Menus: 0
- Rules (ir.rule): 3
- Access CSV entries: 6

## Detected Models

- `HrEmployee`
- `hr.user.work.entry.employee`
- `HrVersion`
- `hr.work.entry`
- `hr.work.entry.type`
- `ResourceCalendar`
- `ResourceCalendarAttendance`
- `ResourceCalendarLeaves`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Work Entries - Models and Relations
class HrEmployee
class "hr.user.work.entry.employee" as hr_user_work_entry_employee
class HrVersion
class "hr.work.entry" as hr_work_entry
class "hr.work.entry.type" as hr_work_entry_type
class ResourceCalendar
class ResourceCalendarAttendance
class ResourceCalendarLeaves
class "res.users" as res_users
hr_user_work_entry_employee --> res_users : many2one
class "hr.employee" as hr_employee
hr_user_work_entry_employee --> hr_employee : many2one
hr_work_entry --> hr_employee : many2one
class "hr.version" as hr_version
hr_work_entry --> hr_version : many2one
hr_work_entry --> hr_work_entry_type : many2one
class "res.company" as res_company
hr_work_entry --> res_company : many2one
class "hr.department" as hr_department
hr_work_entry --> hr_department : many2one
class "res.country" as res_country
hr_work_entry --> res_country : many2one
hr_work_entry_type --> res_country : many2one
ResourceCalendarAttendance --> hr_work_entry_type : many2one
ResourceCalendarLeaves --> hr_work_entry_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





