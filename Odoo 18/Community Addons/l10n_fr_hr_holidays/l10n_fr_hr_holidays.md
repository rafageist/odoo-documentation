<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# France - Time Off

- Version: v18
- Category: community
- Source: odoo/addons/l10n_fr_hr_holidays
- Dependencies: [[Odoo 18/Community Addons/hr_holidays/hr_holidays|hr_holidays]]

## Summary

Management of leaves for part-time workers in France

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrLeave`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - Time Off - Models and Relations
class HrLeave
class ResCompany
class "hr.leave.type" as hr_leave_type
ResCompany --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
