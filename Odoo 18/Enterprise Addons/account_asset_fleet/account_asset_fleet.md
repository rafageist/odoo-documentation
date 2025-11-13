<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Assets/Fleet bridge

- Version: v18
- Category: enterprise
- Source: enterprise18/account_asset_fleet
- Dependencies: [[Odoo 18/Community Addons/account_fleet/account_fleet|account_fleet]], [[Odoo 18/Enterprise Addons/account_asset/account_asset|account_asset]]

## Summary

Manage assets with fleets

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAsset`
- `AccountMove`
- `FleetVehicleLogServices`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Assets/Fleet bridge - Models and Relations
class AccountAsset
class AccountMove
class FleetVehicleLogServices
class "fleet.vehicle" as fleet_vehicle
AccountAsset --> fleet_vehicle : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
