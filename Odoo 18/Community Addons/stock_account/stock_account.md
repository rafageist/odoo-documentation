<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# WMS Accounting

- Version: v18
- Category: community
- Source: odoo/addons/stock_account
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]], [[Odoo 18/Community Addons/account/account|account]]

## Summary

Inventory, Logistic, Valuation, Accounting

## XML Artifacts (detected)

- Views: 25
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 8

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountAnalyticPlan`
- `AccountAnalyticAccount`
- `product.template`
- `ProductProduct`
- `ProductCategory`
- `res.company`
- `StockLocation`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockPicking`
- `StockQuant`
- `stock.valuation.layer`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title WMS Accounting - Models and Relations
class AccountMove
class AccountMoveLine
class AccountAnalyticPlan
class AccountAnalyticAccount
class "product.template" as product_template
class ProductProduct
class ProductCategory
class "res.company" as res_company
class StockLocation
class StockLot
class StockMove
class StockMoveLine
class StockPicking
class StockQuant
class "stock.valuation.layer" as stock_valuation_layer
class "stock.move" as stock_move
AccountMove --> stock_move : many2one
AccountMove --|> stock_valuation_layer : one2many
AccountMoveLine --|> stock_valuation_layer : one2many
class "account.move.line" as account_move_line
AccountMoveLine --> account_move_line : many2one
class "res.currency" as res_currency
ProductProduct --> res_currency : many2one
ProductProduct --|> stock_valuation_layer : one2many
class "account.journal" as account_journal
ProductCategory --> account_journal : many2one
class "account.account" as account_account
ProductCategory --> account_account : many2one
ProductCategory --> account_account : many2one
ProductCategory --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
StockLocation --> account_account : many2one
StockLocation --> account_account : many2one
StockLot --> res_currency : many2one
StockLot --|> stock_valuation_layer : one2many
class "account.move" as account_move
StockMove --|> account_move : one2many
StockMove --|> stock_valuation_layer : one2many
class "account.analytic.line" as account_analytic_line
StockMove .. account_analytic_line : many2many
StockQuant --> res_currency : many2one
stock_valuation_layer --> res_company : many2one
class "product.product" as product_product
stock_valuation_layer --> product_product : many2one
class "product.category" as product_category
stock_valuation_layer --> product_category : many2one
stock_valuation_layer --> product_template : many2one
stock_valuation_layer --> res_currency : many2one
stock_valuation_layer --> stock_valuation_layer : many2one
stock_valuation_layer --|> stock_valuation_layer : one2many
stock_valuation_layer --> stock_move : many2one
stock_valuation_layer --> account_move : many2one
stock_valuation_layer --> account_move_line : many2one
class "stock.warehouse" as stock_warehouse
stock_valuation_layer --> stock_warehouse : many2one
class "stock.lot" as stock_lot
stock_valuation_layer --> stock_lot : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
