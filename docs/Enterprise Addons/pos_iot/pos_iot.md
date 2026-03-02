<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT for PoS

- Scope: Enterprise Addons
- Source: enterprise/pos_iot
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Enterprise Addons/iot/iot|iot]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



