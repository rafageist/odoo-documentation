<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Accounting/Fleet bridge

- Scope: Community Addons
- Source: odoo/addons/account_fleet
- Dependencies: [[docs/Community Addons/fleet/fleet|fleet]], [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





