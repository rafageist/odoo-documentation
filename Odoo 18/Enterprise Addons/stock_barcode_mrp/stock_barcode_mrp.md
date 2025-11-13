<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# MRP Barcode

- Version: v18
- Category: enterprise
- Source: enterprise18/stock_barcode_mrp
- Dependencies: [[Odoo 18/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]], [[Odoo 18/Community Addons/mrp/mrp|mrp]]

## Summary

Process Manufacturing Orders from the barcode application

## XML Artifacts (detected)

- Views: 7
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ManufacturingOrder`
- `Product`
- `StockMove`
- `StockMoveLine`
- `StockPicking`
- `StockPickingType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MRP Barcode - Models and Relations
class ManufacturingOrder
class Product
class StockMove
class StockMoveLine
class StockPicking
class StockPickingType
class "stock.move.line" as stock_move_line
ManufacturingOrder --|> stock_move_line : one2many
ManufacturingOrder --|> stock_move_line : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
