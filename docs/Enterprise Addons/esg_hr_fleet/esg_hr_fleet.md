<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# ESG HR Fleet

- Scope: Enterprise Addons
- Source: enterprise/esg_hr_fleet
- Dependencies: [[docs/Enterprise Addons/esg/esg|esg]], [[docs/Community Addons/hr_fleet/hr_fleet|hr_fleet]]

## Summary

Measure fleet emissions based on your employees' commuting distance and vehicle data.

## XML Artifacts (detected)

- Views: 4
- Actions: 3
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `EsgOtherEmission`
- `FleetVehicleAssignationLog`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title ESG HR Fleet - Models and Relations
class EsgOtherEmission
class FleetVehicleAssignationLog
class ResCompany
class "res.company" as res_company
FleetVehicleAssignationLog --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



