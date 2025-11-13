<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Quality Steps with IoT

- Version: v19
- Category: enterprise
- Source: enterprise19/quality_iot
- Dependencies: [[Odoo 19/Enterprise Addons/iot/iot|iot]], [[Odoo 19/Enterprise Addons/quality/quality|quality]]

## Summary

Quality steps and IoT devices

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IotDevice`
- `QualityPoint`
- `QualityCheck`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Quality Steps with IoT - Models and Relations
class IotDevice
class QualityPoint
class QualityCheck
class "quality.point" as quality_point
IotDevice --|> quality_point : one2many
class "iot.device" as iot_device
QualityPoint --> iot_device : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
