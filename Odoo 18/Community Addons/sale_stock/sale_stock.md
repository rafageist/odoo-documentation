<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sales and Warehouse Management

- Version: v18
- Category: community
- Source: odoo/addons/sale_stock
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Quotation, Sales Orders, Delivery & Invoicing Control

## XML Artifacts (detected)

- Views: 14
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 18

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `company`
- `Users`
- `SaleOrder`
- `SaleOrderLine`
- `StockRoute`
- `StockMove`
- `StockMoveLine`
- `ProcurementGroup`
- `StockRule`
- `StockPicking`
- `StockLot`
- `Warehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales and Warehouse Management - Models and Relations
class AccountMove
class AccountMoveLine
class ProductTemplate
class company
class Users
class SaleOrder
class SaleOrderLine
class StockRoute
class StockMove
class StockMoveLine
class ProcurementGroup
class StockRule
class StockPicking
class StockLot
class Warehouse
class "stock.warehouse" as stock_warehouse
Users --> stock_warehouse : many2one
class "account.incoterms" as account_incoterms
SaleOrder --> account_incoterms : many2one
SaleOrder --> stock_warehouse : many2one
class "stock.picking" as stock_picking
SaleOrder --|> stock_picking : one2many
class "procurement.group" as procurement_group
SaleOrder --> procurement_group : many2one
class "stock.route" as stock_route
SaleOrderLine --> stock_route : many2one
class "stock.move" as stock_move
SaleOrderLine --|> stock_move : one2many
SaleOrderLine --> stock_warehouse : many2one
class "sale.order.line" as sale_order_line
StockMove --> sale_order_line : many2one
class "sale.order" as sale_order
ProcurementGroup --> sale_order : many2one
StockPicking --> sale_order : many2one
StockLot .. sale_order : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
