<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# MRP features for Quality Control

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/quality_mrp
- Dependencies: [[Odoo 19/Enterprise Addons/quality_control/quality_control|quality_control]], [[Odoo 19/Community Addons/mrp/mrp|mrp]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

