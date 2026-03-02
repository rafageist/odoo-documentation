<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales and Warehouse Management

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/sale_stock
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Quotation, Sales Orders, Delivery & Invoicing Control

## XML Artifacts (detected)

- Views: 14
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 16

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `ResCompany`
- `ResUsers`
- `SaleOrder`
- `SaleOrderLine`
- `StockRoute`
- `StockMove`
- `StockMoveLine`
- `StockRule`
- `StockPicking`
- `StockLot`
- `StockReference`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales and Warehouse Management - Models and Relations
class AccountMove
class AccountMoveLine
class ProductTemplate
class ResCompany
class ResUsers
class SaleOrder
class SaleOrderLine
class StockRoute
class StockMove
class StockMoveLine
class StockRule
class StockPicking
class StockLot
class StockReference
class "stock.warehouse" as stock_warehouse
ResUsers --> stock_warehouse : many2one
class "account.incoterms" as account_incoterms
SaleOrder --> account_incoterms : many2one
SaleOrder --> stock_warehouse : many2one
class "stock.picking" as stock_picking
SaleOrder --|> stock_picking : one2many
class "stock.reference" as stock_reference
SaleOrder .. stock_reference : many2many
class "stock.route" as stock_route
SaleOrderLine .. stock_route : many2many
class "stock.move" as stock_move
SaleOrderLine --|> stock_move : one2many
SaleOrderLine --> stock_warehouse : many2one
class "sale.order.line" as sale_order_line
StockMove --> sale_order_line : many2one
class "sale.order" as sale_order
StockPicking --> sale_order : many2one
StockLot .. sale_order : many2many
StockReference .. sale_order : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

