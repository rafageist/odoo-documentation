<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Fleet History

- Version: v18
- Category: community
- Source: odoo/addons/hr_fleet
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/fleet/fleet|fleet]]

## Summary

Get history of driven cars by employees

## XML Artifacts (detected)

- Views: 17
- Actions: 0
- Menus: 0
- Rules (ir.rule): 5
- Access CSV entries: 1

## Detected Models

- `Employee`
- `EmployeePublic`
- `FleetVehicle`
- `FleetVehicleAssignationLog`
- `FleetVehicleLogContract`
- `FleetVehicleLogServices`
- `FleetVehicleOdometer`
- `MailActivityPlanTemplate`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Fleet History - Models and Relations
class Employee
class EmployeePublic
class FleetVehicle
class FleetVehicleAssignationLog
class FleetVehicleLogContract
class FleetVehicleLogServices
class FleetVehicleOdometer
class MailActivityPlanTemplate
class User
class "fleet.vehicle" as fleet_vehicle
Employee --|> fleet_vehicle : one2many
class "hr.employee" as hr_employee
FleetVehicle --> hr_employee : many2one
FleetVehicle --> hr_employee : many2one
FleetVehicleAssignationLog --> hr_employee : many2one
FleetVehicleLogServices --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
