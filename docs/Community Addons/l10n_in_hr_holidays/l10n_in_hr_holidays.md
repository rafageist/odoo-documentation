<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# India - Time Off

- Scope: Community Addons
- Source: odoo/addons/l10n_in_hr_holidays
- Dependencies: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





