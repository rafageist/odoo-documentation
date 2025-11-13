<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# India - Time Off

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_in_hr_holidays
- Dependencies: [[Odoo 19/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Leave Management of Indian Localization

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `HrEmployees`
- `HrLeave`
- `HrLeaveType`
- `l10n.in.hr.leave.optional.holiday`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title India - Time Off - Models and Relations
class HrEmployees
class HrLeave
class HrLeaveType
class "l10n.in.hr.leave.optional.holiday" as l10n_in_hr_leave_optional_holiday
class "res.company" as res_company
l10n_in_hr_leave_optional_holiday --> res_company : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
