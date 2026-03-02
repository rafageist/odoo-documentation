<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Repair features for Quality Control

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/quality_repair
- Dependencies: [[Odoo 19/Enterprise Addons/quality_control/quality_control|quality_control]], [[Odoo 19/Community Addons/repair/repair|repair]]

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
- `RepairOrder`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Repair features for Quality Control - Models and Relations
class QualityPoint
class QualityCheck
class QualityAlert
class RepairOrder
class "repair.order" as repair_order
QualityCheck --> repair_order : many2one
QualityAlert --> repair_order : many2one
class "quality.check" as quality_check
RepairOrder --|> quality_check : one2many
class "quality.alert" as quality_alert
RepairOrder --|> quality_alert : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

