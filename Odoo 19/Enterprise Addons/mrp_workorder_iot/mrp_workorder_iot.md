<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# IoT features for Work Order

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/mrp_workorder_iot
- Dependencies: [[Odoo 19/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 19/Enterprise Addons/quality_iot/quality_iot|quality_iot]]

## Summary

Steps in MRP work orders with IoT devices

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `MrpWorkcenter`
- `iot.trigger`
- `IotDevice`
- `QualityCheck`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT features for Work Order - Models and Relations
class MrpWorkcenter
class "iot.trigger" as iot_trigger
class IotDevice
class QualityCheck
MrpWorkcenter --|> iot_trigger : one2many
class "iot.device" as iot_device
iot_trigger --> iot_device : many2one
class "mrp.workcenter" as mrp_workcenter
iot_trigger --> mrp_workcenter : many2one
IotDevice --|> iot_trigger : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

