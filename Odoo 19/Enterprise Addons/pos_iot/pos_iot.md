<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# IoT for PoS

- Version: v19
- Category: enterprise
- Source: enterprise19/pos_iot
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Enterprise Addons/iot/iot|iot]]

## Summary

Use IoT Devices in the PoS

## XML Artifacts (detected)

- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `iot.box`
- `iot.device`
- `PosConfig`
- `PosPaymentMethod`
- `PosPrinter`
- `PosSession`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT for PoS - Models and Relations
class "iot.box" as iot_box
class "iot.device" as iot_device
class PosConfig
class PosPaymentMethod
class PosPrinter
class PosSession
class "pos.config" as pos_config
iot_box .. pos_config : many2many
iot_device .. pos_config : many2many
PosConfig --> iot_device : many2one
PosConfig --> iot_device : many2one
PosConfig .. iot_device : many2many
PosConfig --> iot_device : many2one
PosConfig .. iot_device : many2many
PosConfig .. iot_device : many2many
PosPaymentMethod --> iot_device : many2one
PosPrinter --> iot_device : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
