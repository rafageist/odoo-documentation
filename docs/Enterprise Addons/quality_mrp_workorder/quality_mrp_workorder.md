<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# MRP features for Quality Control

- Scope: Enterprise Addons
- Source: enterprise/quality_mrp_workorder
- Dependencies: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]], [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[docs/Community Addons/barcodes/barcodes|barcodes]]

## Summary

Quality Management with MRP

## XML Artifacts (detected)

- Views: 11
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MrpProduction`
- `MrpWorkorder`
- `ProductTemplate`
- `ProductProduct`
- `QualityPoint`
- `QualityCheck`
- `StockLot`
- `StockMoveLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title MRP features for Quality Control - Models and Relations
class MrpProduction
class MrpWorkorder
class ProductTemplate
class ProductProduct
class QualityPoint
class QualityCheck
class StockLot
class StockMoveLine
class "quality.check" as quality_check
MrpProduction --|> quality_check : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



