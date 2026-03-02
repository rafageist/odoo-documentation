<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# POS Self Order IoT

- Scope: Enterprise Addons
- Source: enterprise/pos_self_order_iot
- Dependencies: [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



