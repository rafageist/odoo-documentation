<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# IoT for Delivery

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/delivery_iot
- Dependencies: [[Odoo 19/Enterprise Addons/iot/iot|iot]], [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Use IoT devices in delivery operations

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 4
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IotDevice`
- `IrActionReport`
- `StockPickingType`
- `StockPicking`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT for Delivery - Models and Relations
class IotDevice
class IrActionReport
class StockPickingType
class StockPicking
class "stock.picking.type" as stock_picking_type
IotDevice .. stock_picking_type : many2many
class "iot.device" as iot_device
StockPickingType .. iot_device : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

