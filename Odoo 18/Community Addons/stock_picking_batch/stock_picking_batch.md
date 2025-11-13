<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Warehouse Management: Batch Transfer

- Version: v18
- Category: community
- Source: odoo/addons/stock_picking_batch
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]]
## XML Artifacts (detected)

- Views: 22
- Actions: 8
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `StockMove`
- `StockMoveLine`
- `StockPickingType`
- `StockPicking`
- `stock.picking.batch`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Warehouse Management: Batch Transfer - Models and Relations
class StockMove
class StockMoveLine
class StockPickingType
class StockPicking
class "stock.picking.batch" as stock_picking_batch
class StockWarehouse
class "product.category" as product_category
StockPickingType .. product_category : many2many
class "stock.location" as stock_location
StockPickingType .. stock_location : many2many
StockPicking --> stock_picking_batch : many2one
class "res.users" as res_users
stock_picking_batch --> res_users : many2one
class "res.company" as res_company
stock_picking_batch --> res_company : many2one
class "stock.picking" as stock_picking
stock_picking_batch --|> stock_picking : one2many
stock_picking_batch --|> stock_picking : one2many
class "stock.move" as stock_move
stock_picking_batch --|> stock_move : one2many
class "stock.move.line" as stock_move_line
stock_picking_batch --|> stock_move_line : one2many
class "stock.picking.type" as stock_picking_type
stock_picking_batch --> stock_picking_type : many2one
class "stock.warehouse" as stock_warehouse
stock_picking_batch --> stock_warehouse : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
