
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Quality

- Scope: Enterprise Addons
- Source: enterprise/quality_control
- Dependencies: [[docs/Enterprise Addons/quality/quality|quality]], [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Control the quality of your products

## XML Artifacts (detected)

- Views: 36
- Actions: 20
- Menus: 18
- Rules (ir.rule): 2
- Access CSV entries: 5

## Detected Models

- `QualityPoint`
- `QualityCheck`
- `QualityAlert`
- `ProductTemplate`
- `ProductProduct`
- `quality.check.spreadsheet`
- `quality.spreadsheet.template`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Quality - Models and Relations
class QualityPoint
class QualityCheck
class QualityAlert
class ProductTemplate
class ProductProduct
class "quality.check.spreadsheet" as quality_check_spreadsheet
class "quality.spreadsheet.template" as quality_spreadsheet_template
class StockLot
class StockMove
class StockMoveLine
class StockPicking
QualityPoint --> quality_spreadsheet_template : many2one
class "stock.move.line" as stock_move_line
QualityCheck --> stock_move_line : many2one
class "stock.lot" as stock_lot
QualityCheck --> stock_lot : many2one
QualityCheck --> quality_check_spreadsheet : many2one
class "product.product" as product_product
QualityCheck .. product_product : many2many
QualityCheck --> quality_spreadsheet_template : many2one
class "res.company" as res_company
quality_check_spreadsheet --> res_company : many2one
quality_spreadsheet_template --> res_company : many2one
class "quality.check" as quality_check
StockMoveLine --|> quality_check : one2many
StockPicking --|> quality_check : one2many
class "quality.alert" as quality_alert
StockPicking --|> quality_alert : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

