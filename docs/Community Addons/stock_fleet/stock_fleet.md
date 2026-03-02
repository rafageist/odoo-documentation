
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Stock Transport

- Scope: Community Addons
- Source: odoo/addons/stock_fleet
- Dependencies: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]], [[docs/Community Addons/fleet/fleet|fleet]]

## Summary

Stock Transport: Dispatch Management System

## XML Artifacts (detected)

- Views: 13
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `FleetVehicleModelCategory`
- `StockPickingType`
- `StockPicking`
- `StockPickingBatch`
- `StockWarehouse`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Stock Transport - Models and Relations
class FleetVehicleModelCategory
class StockPickingType
class StockPicking
class StockPickingBatch
class StockWarehouse
class "stock.location" as stock_location
StockPickingType .. stock_location : many2many
class "fleet.vehicle" as fleet_vehicle
StockPickingBatch --> fleet_vehicle : many2one
class "fleet.vehicle.model.category" as fleet_vehicle_model_category
StockPickingBatch --> fleet_vehicle_model_category : many2one
StockPickingBatch --> stock_location : many2one
class "res.partner" as res_partner
StockPickingBatch --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



