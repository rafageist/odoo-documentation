<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Work Entries - Planning

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_work_entry_contract_planning
- Dependencies: [[Odoo 18/Enterprise Addons/hr_work_entry_contract_enterprise/hr_work_entry_contract_enterprise|hr_work_entry_contract_enterprise]], [[Odoo 18/Enterprise Addons/planning/planning|planning]]

## Summary

Create work entries from the employee's planning

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrContract`
- `HrWorkEntry`
- `PlanningSlot`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Planning - Models and Relations
class HrContract
class HrWorkEntry
class PlanningSlot
class "planning.slot" as planning_slot
HrWorkEntry --> planning_slot : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
