<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Work Entries - Planning

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/hr_work_entry_planning
- Dependencies: [[Odoo 19/Enterprise Addons/hr_work_entry_enterprise/hr_work_entry_enterprise|hr_work_entry_enterprise]], [[Odoo 19/Enterprise Addons/planning/planning|planning]]

## Summary

Create work entries from the employee's planning

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrVersion`
- `HrWorkEntry`
- `PlanningSlot`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Work Entries - Planning - Models and Relations
class HrVersion
class HrWorkEntry
class PlanningSlot
class "planning.slot" as planning_slot
HrWorkEntry --> planning_slot : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

