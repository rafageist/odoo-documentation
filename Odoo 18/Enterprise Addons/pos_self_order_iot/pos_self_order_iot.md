<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# POS Self Order IoT

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_self_order_iot
- Dependencies: [[Odoo 18/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 18/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

## Summary

IoT in PoS Kiosk

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IotBox`
- `PosConfig`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS Self Order IoT - Models and Relations
class IotBox
class PosConfig
class "pos.config" as pos_config
IotBox --> pos_config : many2one
class "iot.box" as iot_box
PosConfig --|> iot_box : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
