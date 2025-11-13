<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Work Entries - Attendance

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_work_entry_contract_attendance
- Dependencies: [[Odoo 18/Community Addons/hr_work_entry_contract/hr_work_entry_contract|hr_work_entry_contract]], [[Odoo 18/Community Addons/hr_attendance/hr_attendance|hr_attendance]]

## Summary

Create work entries from the employee's attendances

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrAttendance`
- `HrContract`
- `HrWorkEntry`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Attendance - Models and Relations
class HrAttendance
class HrContract
class HrWorkEntry
class "hr.attendance" as hr_attendance
HrWorkEntry --> hr_attendance : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
