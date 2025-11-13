<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# IoT features for Work Order

- Version: v18
- Category: enterprise
- Source: enterprise18/mrp_workorder_iot
- Dependencies: [[Odoo 18/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 18/Enterprise Addons/quality_iot/quality_iot|quality_iot]]

## Summary

Steps in MRP work orders with IoT devices

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `MrpWorkcenter`
- `iot.trigger`
- `IoTDevice`
- `QualityCheck`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IoT features for Work Order - Models and Relations
class MrpWorkcenter
class "iot.trigger" as iot_trigger
class IoTDevice
class QualityCheck
MrpWorkcenter --|> iot_trigger : one2many
class "iot.device" as iot_device
iot_trigger --> iot_device : many2one
class "mrp.workcenter" as mrp_workcenter
iot_trigger --> mrp_workcenter : many2one
IoTDevice --|> iot_trigger : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
