<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Assets/Fleet bridge

- Scope: Enterprise Addons
- Source: enterprise/account_asset_fleet
- Dependencies: [[docs/Community Addons/account_fleet/account_fleet|account_fleet]], [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]

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
!include ../../../templates/DiagramStyles.puml
title Assets/Fleet bridge - Models and Relations
class AccountAsset
class AccountMove
class FleetVehicleLogServices
class "fleet.vehicle" as fleet_vehicle
AccountAsset --> fleet_vehicle : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



