<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# MRP Barcode

- Scope: Enterprise Addons
- Source: enterprise/stock_barcode_mrp
- Dependencies: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]], [[docs/Community Addons/mrp/mrp|mrp]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



