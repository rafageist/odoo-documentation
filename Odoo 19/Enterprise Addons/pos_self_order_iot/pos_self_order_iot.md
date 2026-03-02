<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# POS Self Order IoT

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_self_order_iot
- Dependencies: [[Odoo 19/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 19/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

## Summary

IoT in PoS Kiosk

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IotBox`
- `PosConfig`
- `PosPaymentMethod`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS Self Order IoT - Models and Relations
class IotBox
class PosConfig
class PosPaymentMethod
class "pos.config" as pos_config
IotBox --> pos_config : many2one
class "iot.box" as iot_box
PosConfig --|> iot_box : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

