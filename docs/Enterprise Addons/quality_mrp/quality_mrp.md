<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# MRP features for Quality Control

- Scope: Enterprise Addons
- Source: enterprise/quality_mrp
- Dependencies: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]], [[docs/Community Addons/mrp/mrp|mrp]]

## Summary

Quality Management with MRP

## XML Artifacts (detected)

- Views: 2
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MrpProduction`
- `QualityPoint`
- `QualityCheck`
- `QualityAlert`
- `StockMove`
- `StockMoveLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title MRP features for Quality Control - Models and Relations
class MrpProduction
class QualityPoint
class QualityCheck
class QualityAlert
class StockMove
class StockMoveLine
class "quality.check" as quality_check
MrpProduction --|> quality_check : one2many
class "quality.alert" as quality_alert
MrpProduction --|> quality_alert : one2many
class "mrp.production" as mrp_production
QualityCheck --> mrp_production : many2one
QualityAlert --> mrp_production : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



