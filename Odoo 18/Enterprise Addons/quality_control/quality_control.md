<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Quality

- Version: v18
- Category: enterprise
- Source: enterprise18/quality_control
- Dependencies: [[Odoo 18/Enterprise Addons/quality/quality|quality]], [[Odoo 18/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Control the quality of your products

## XML Artifacts (detected)

- Views: 37
- Actions: 20
- Menus: 18
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `QualityPoint`
- `QualityCheck`
- `QualityAlert`
- `ProductTemplate`
- `ProductProduct`
- `quality.check.spreadsheet`
- `quality.spreadsheet.template`
- `ProductionLot`
- `StockMove`
- `StockMoveLine`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Quality - Models and Relations
class QualityPoint
class QualityCheck
class QualityAlert
class ProductTemplate
class ProductProduct
class "quality.check.spreadsheet" as quality_check_spreadsheet
class "quality.spreadsheet.template" as quality_spreadsheet_template
class ProductionLot
class StockMove
class StockMoveLine
class StockPicking
class "stock.location" as stock_location
QualityPoint .. stock_location : many2many
QualityPoint --> quality_spreadsheet_template : many2one
class "stock.move.line" as stock_move_line
QualityCheck --> stock_move_line : many2one
QualityCheck --> stock_location : many2one
class "stock.lot" as stock_lot
QualityCheck --> stock_lot : many2one
QualityCheck --> quality_check_spreadsheet : many2one
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
