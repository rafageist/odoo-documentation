<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Fleet History

- Scope: Community Addons
- Source: odoo/addons/hr_fleet
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/fleet/fleet|fleet]]

## Summary

Get history of driven cars by employees

## XML Artifacts (detected)

- Views: 16
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `FleetVehicle`
- `FleetVehicleAssignationLog`
- `FleetVehicleLogContract`
- `FleetVehicleLogServices`
- `FleetVehicleOdometer`
- `IrAttachment`
- `MailActivityPlanTemplate`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Fleet History - Models and Relations
class HrEmployee
class HrEmployeePublic
class FleetVehicle
class FleetVehicleAssignationLog
class FleetVehicleLogContract
class FleetVehicleLogServices
class FleetVehicleOdometer
class IrAttachment
class MailActivityPlanTemplate
class "fleet.vehicle" as fleet_vehicle
HrEmployee --|> fleet_vehicle : one2many
class "hr.employee" as hr_employee
FleetVehicle --> hr_employee : many2one
FleetVehicle --> hr_employee : many2one
FleetVehicleAssignationLog --> hr_employee : many2one
FleetVehicleLogServices --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





