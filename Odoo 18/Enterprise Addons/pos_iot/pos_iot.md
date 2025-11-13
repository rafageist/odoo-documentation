<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# IoT for PoS

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_iot
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Enterprise Addons/iot/iot|iot]]

## Summary

Use IoT Devices in the PoS

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `iot.box`
- `iot.device`
- `PosConfig`
- `PoSPaymentMethod`
- `RestaurantPrinter`
- `PosSession`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT for PoS - Models and Relations
class "iot.box" as iot_box
class "iot.device" as iot_device
class PosConfig
class PoSPaymentMethod
class RestaurantPrinter
class PosSession
PosConfig --> iot_device : many2one
PosConfig --> iot_device : many2one
PosConfig .. iot_device : many2many
PosConfig --> iot_device : many2one
PosConfig .. iot_device : many2many
PosConfig .. iot_device : many2many
PoSPaymentMethod .. iot_device : many2many
PoSPaymentMethod --> iot_device : many2one
RestaurantPrinter --> iot_device : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
