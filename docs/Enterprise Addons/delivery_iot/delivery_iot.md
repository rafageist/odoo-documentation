<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT for Delivery

- Scope: Enterprise Addons
- Source: enterprise/delivery_iot
- Dependencies: [[docs/Enterprise Addons/iot/iot|iot]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



