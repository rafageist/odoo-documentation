<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# WMS Landed Costs

- Version: v18
- Category: community
- Source: odoo/addons/stock_landed_costs
- Dependencies: [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 18/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

## Summary

Landed Costs

## XML Artifacts (detected)

- Views: 9
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `PurchaseOrderLine`
- `ResCompany`
- `stock.landed.cost`
- `stock.landed.cost.lines`
- `stock.valuation.adjustment.lines`
- `StockMove`
- `StockValuationLayer`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title WMS Landed Costs - Models and Relations
class AccountMove
class AccountMoveLine
class ProductTemplate
class PurchaseOrderLine
class ResCompany
class "stock.landed.cost" as stock_landed_cost
class "stock.landed.cost.lines" as stock_landed_cost_lines
class "stock.valuation.adjustment.lines" as stock_valuation_adjustment_lines
class StockMove
class StockValuationLayer
AccountMove --|> stock_landed_cost : one2many
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
class "stock.picking" as stock_picking
stock_landed_cost .. stock_picking : many2many
stock_landed_cost --|> stock_landed_cost_lines : one2many
stock_landed_cost --|> stock_valuation_adjustment_lines : one2many
class "account.move" as account_move
stock_landed_cost --> account_move : many2one
stock_landed_cost --> account_journal : many2one
class "res.company" as res_company
stock_landed_cost --> res_company : many2one
class "stock.valuation.layer" as stock_valuation_layer
stock_landed_cost --|> stock_valuation_layer : one2many
stock_landed_cost --> account_move : many2one
class "res.currency" as res_currency
stock_landed_cost --> res_currency : many2one
stock_landed_cost_lines --> stock_landed_cost : many2one
class "product.product" as product_product
stock_landed_cost_lines --> product_product : many2one
class "account.account" as account_account
stock_landed_cost_lines --> account_account : many2one
stock_landed_cost_lines --> res_currency : many2one
stock_valuation_adjustment_lines --> stock_landed_cost : many2one
stock_valuation_adjustment_lines --> stock_landed_cost_lines : many2one
class "stock.move" as stock_move
stock_valuation_adjustment_lines --> stock_move : many2one
stock_valuation_adjustment_lines --> product_product : many2one
stock_valuation_adjustment_lines --> res_currency : many2one
StockValuationLayer --> stock_landed_cost : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
