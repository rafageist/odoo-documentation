<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# IoT for Delivery

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_iot
- Dependencies: [[Odoo 18/Enterprise Addons/iot/iot|iot]], [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Use IoT devices in delivery operations

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IotDevice`
- `IrActionReport`
- `PickingType`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT for Delivery - Models and Relations
class IotDevice
class IrActionReport
class PickingType
class StockPicking
class "stock.picking.type" as stock_picking_type
IotDevice .. stock_picking_type : many2many
class "iot.device" as iot_device
PickingType .. iot_device : many2many
StockPicking .. iot_device : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
