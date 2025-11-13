<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Time Off in Payslips

- Version: v18
- Category: community
- Source: odoo/addons/hr_work_entry_holidays
- Dependencies: [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]], [[Odoo 18/Community Addons/hr_holidays_contract/hr_holidays_contract|hr_holidays_contract]], [[Odoo 18/Community Addons/hr_work_entry_contract/hr_work_entry_contract|hr_work_entry_contract]]

## Summary

Manage Time Off in Payslips

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrContract`
- `HrLeaveType`
- `HrLeave`
- `HrWorkEntry`
- `HrWorkEntryType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Time Off in Payslips - Models and Relations
class HrContract
class HrLeaveType
class HrLeave
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
