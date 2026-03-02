<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# MRP Barcode

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/stock_barcode_mrp
- Dependencies: [[Odoo 19/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]], [[Odoo 19/Community Addons/mrp/mrp|mrp]]

## Summary

Process Manufacturing Orders from the barcode application

## XML Artifacts (detected)

- Views: 7
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MrpProduction`
- `ProductProduct`
- `StockMove`
- `StockMoveLine`
- `StockPicking`
- `StockPickingType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MRP Barcode - Models and Relations
class MrpProduction
class ProductProduct
class StockMove
class StockMoveLine
class StockPicking
class StockPickingType
class "stock.move.line" as stock_move_line
MrpProduction --|> stock_move_line : one2many
MrpProduction --|> stock_move_line : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

