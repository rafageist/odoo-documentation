<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Fleet History

- Version: v19
- Category: community
- Source: odoo19/addons/hr_fleet
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/fleet/fleet|fleet]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
