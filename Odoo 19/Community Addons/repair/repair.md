<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Repairs

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/repair
- Dependencies: [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Repair damaged products

## XML Artifacts (detected)

- Views: 18
- Actions: 9
- Menus: 8
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `ProductProduct`
- `ProductTemplate`
- `repair.order`
- `repair.tags`
- `SaleOrder`
- `SaleOrderLine`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockPickingType`
- `StockPicking`
- `StockWarehouse`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Repairs - Models and Relations
class ProductProduct
class ProductTemplate
class "repair.order" as repair_order
class "repair.tags" as repair_tags
class SaleOrder
class SaleOrderLine
class StockLot
class StockMove
class StockMoveLine
class StockPickingType
class StockPicking
class StockWarehouse
class "res.company" as res_company
repair_order --> res_company : many2one
class "res.partner" as res_partner
repair_order --> res_partner : many2one
class "res.users" as res_users
repair_order --> res_users : many2one
repair_order .. repair_tags : many2many
class "stock.move" as stock_move
repair_order --> stock_move : many2one
class "product.product" as product_product
repair_order --> product_product : many2one
class "uom.uom" as uom_uom
repair_order .. uom_uom : many2many
repair_order --> uom_uom : many2one
class "stock.lot" as stock_lot
repair_order --> stock_lot : many2one
class "stock.picking.type" as stock_picking_type
repair_order --> stock_picking_type : many2one
class "stock.reference" as stock_reference
repair_order .. stock_reference : many2many
class "stock.location" as stock_location
repair_order --> stock_location : many2one
repair_order --> stock_location : many2one
repair_order --> stock_location : many2one
repair_order --> stock_location : many2one
repair_order --> stock_location : many2one
repair_order --> stock_location : many2one
repair_order --|> stock_move : one2many
class "sale.order" as sale_order
repair_order --> sale_order : many2one
class "sale.order.line" as sale_order_line
repair_order --> sale_order_line : many2one
class "stock.picking" as stock_picking
repair_order --> stock_picking : many2one
repair_order --|> product_product : one2many
repair_order --|> stock_lot : one2many
SaleOrder --|> repair_order : one2many
StockLot .. repair_order : many2many
StockMove --> repair_order : many2one
StockPickingType --> stock_location : many2one
StockPickingType --> stock_location : many2one
StockPickingType --> stock_location : many2one
StockPickingType --> stock_location : many2one
StockPicking --|> repair_order : one2many
StockWarehouse --> stock_picking_type : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


