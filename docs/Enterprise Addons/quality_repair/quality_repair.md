<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Repair features for Quality Control

- Scope: Enterprise Addons
- Source: enterprise/quality_repair
- Dependencies: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]], [[docs/Community Addons/repair/repair|repair]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



