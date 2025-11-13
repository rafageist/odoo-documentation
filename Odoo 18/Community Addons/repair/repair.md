<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Repairs

- Version: v18
- Category: community
- Source: odoo/addons/repair
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Repair damaged products

## XML Artifacts (detected)

- Views: 19
- Actions: 10
- Menus: 9
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `Product`
- `ProductTemplate`
- `repair.order`
- `repair.tags`
- `SaleOrder`
- `SaleOrderLine`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `PickingType`
- `Picking`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Repairs - Models and Relations
class Product
class ProductTemplate
class "repair.order" as repair_order
class "repair.tags" as repair_tags
class SaleOrder
class SaleOrderLine
class StockLot
class StockMove
class StockMoveLine
class PickingType
class Picking
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
repair_order --> uom_uom : many2one
class "stock.lot" as stock_lot
repair_order --> stock_lot : many2one
class "stock.picking.type" as stock_picking_type
repair_order --> stock_picking_type : many2one
class "procurement.group" as procurement_group
repair_order --> procurement_group : many2one
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
PickingType --> stock_location : many2one
PickingType --> stock_location : many2one
PickingType --> stock_location : many2one
PickingType --> stock_location : many2one
PickingType --|> stock_picking_type : one2many
Picking --|> repair_order : one2many
StockWarehouse --> stock_picking_type : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
