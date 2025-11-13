<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Stock Transport

- Version: v19
- Category: community
- Source: odoo19/addons/stock_fleet
- Dependencies: [[Odoo 19/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]], [[Odoo 19/Community Addons/fleet/fleet|fleet]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
