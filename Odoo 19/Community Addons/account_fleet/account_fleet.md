<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Accounting/Fleet bridge

- Version: v19
- Category: community
- Source: odoo19/addons/account_fleet
- Dependencies: [[Odoo 19/Community Addons/fleet/fleet|fleet]], [[Odoo 19/Community Addons/account/account|account]]

## Summary

Manage accounting with fleets

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `FleetVehicle`
- `FleetVehicleLogServices`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Accounting/Fleet bridge - Models and Relations
class AccountMove
class AccountMoveLine
class FleetVehicle
class FleetVehicleLogServices
class "fleet.vehicle" as fleet_vehicle
AccountMoveLine --> fleet_vehicle : many2one
class "fleet.vehicle.log.services" as fleet_vehicle_log_services
AccountMoveLine --|> fleet_vehicle_log_services : one2many
class "account.move" as account_move
FleetVehicle --|> account_move : one2many
class "account.move.line" as account_move_line
FleetVehicleLogServices --> account_move_line : many2one
FleetVehicleLogServices --> fleet_vehicle : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
