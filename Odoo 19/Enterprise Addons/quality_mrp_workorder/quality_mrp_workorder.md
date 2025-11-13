<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# MRP features for Quality Control

- Version: v19
- Category: enterprise
- Source: enterprise19/quality_mrp_workorder
- Dependencies: [[Odoo 19/Enterprise Addons/quality_control/quality_control|quality_control]], [[Odoo 19/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 19/Community Addons/barcodes/barcodes|barcodes]]

## Summary

Quality Management with MRP

## XML Artifacts (detected)

- Views: 10
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
