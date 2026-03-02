<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Work Entries - Planning

- Scope: Enterprise Addons
- Source: enterprise/hr_work_entry_planning
- Dependencies: [[docs/Enterprise Addons/hr_work_entry_enterprise/hr_work_entry_enterprise|hr_work_entry_enterprise]], [[docs/Enterprise Addons/planning/planning|planning]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



