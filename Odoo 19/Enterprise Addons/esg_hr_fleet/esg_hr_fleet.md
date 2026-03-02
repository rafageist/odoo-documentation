<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# ESG HR Fleet

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/esg_hr_fleet
- Dependencies: [[Odoo 19/Enterprise Addons/esg/esg|esg]], [[Odoo 19/Community Addons/hr_fleet/hr_fleet|hr_fleet]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

