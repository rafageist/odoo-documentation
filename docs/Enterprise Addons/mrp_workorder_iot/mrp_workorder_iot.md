
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT features for Work Order

- Scope: Enterprise Addons
- Source: enterprise/mrp_workorder_iot
- Dependencies: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[docs/Enterprise Addons/quality_iot/quality_iot|quality_iot]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

