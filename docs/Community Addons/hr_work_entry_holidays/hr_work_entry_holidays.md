<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Time Off in Payslips

- Scope: Community Addons
- Source: odoo/addons/hr_work_entry_holidays
- Dependencies: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]], [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]

## Summary

Manage Time Off in Payslips

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrLeaveType`
- `HrLeave`
- `HrVersion`
- `HrWorkEntry`
- `HrWorkEntryType`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Time Off in Payslips - Models and Relations
class HrLeaveType
class HrLeave
class HrVersion
class HrWorkEntry
class HrWorkEntryType
class "hr.work.entry.type" as hr_work_entry_type
HrLeaveType --> hr_work_entry_type : many2one
class "hr.leave" as hr_leave
HrWorkEntry --> hr_leave : many2one
class "hr.leave.type" as hr_leave_type
HrWorkEntryType --|> hr_leave_type : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





