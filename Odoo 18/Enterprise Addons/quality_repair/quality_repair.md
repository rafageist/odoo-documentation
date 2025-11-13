<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Repair features for Quality Control

- Version: v18
- Category: enterprise
- Source: enterprise18/quality_repair
- Dependencies: [[Odoo 18/Enterprise Addons/quality_control/quality_control|quality_control]], [[Odoo 18/Community Addons/repair/repair|repair]]

## Summary

Quality Management with Repair

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `QualityPoint`
- `QualityCheck`
- `QualityAlert`
- `Repair`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Repair features for Quality Control - Models and Relations
class QualityPoint
class QualityCheck
class QualityAlert
class Repair
class "repair.order" as repair_order
QualityCheck --> repair_order : many2one
QualityAlert --> repair_order : many2one
class "quality.check" as quality_check
Repair --|> quality_check : one2many
class "quality.alert" as quality_alert
Repair --|> quality_alert : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
