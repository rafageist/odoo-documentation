<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# WMS Accounting

- Scope: Community Addons
- Source: odoo/addons/stock_account
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/account/account|account]]

## Summary

Inventory, Logistic, Valuation, Accounting

## XML Artifacts (detected)

- Views: 19
- Actions: 5
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 9

## Detected Models

- `AccountAccount`
- `AccountMove`
- `AccountMoveLine`
- `AccountAnalyticPlan`
- `AccountAnalyticAccount`
- `ProductTemplate`
- `ProductProduct`
- `ProductCategory`
- `product.value`
- `ResCompany`
- `StockLocation`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockPicking`
- `StockPickingType`
- `StockQuant`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WMS Accounting - Models and Relations
class AccountAccount
class AccountMove
class AccountMoveLine
class AccountAnalyticPlan
class AccountAnalyticAccount
class ProductTemplate
class ProductProduct
class ProductCategory
class "product.value" as product_value
class ResCompany
class StockLocation
class StockLot
class StockMove
class StockMoveLine
class StockPicking
class StockPickingType
class StockQuant
class "account.account" as account_account
AccountAccount --> account_account : many2one
AccountAccount --> account_account : many2one
class "stock.move" as stock_move
AccountMove --|> stock_move : one2many
class "account.move.line" as account_move_line
AccountMoveLine --> account_move_line : many2one
ProductTemplate --> account_account : many2one
class "res.currency" as res_currency
ProductProduct --> res_currency : many2one
class "account.journal" as account_journal
ProductCategory --> account_journal : many2one
ProductCategory --> account_account : many2one
ProductCategory --> account_account : many2one
class "product.product" as product_product
product_value --> product_product : many2one
class "stock.lot" as stock_lot
product_value --> stock_lot : many2one
product_value --> stock_move : many2one
class "res.company" as res_company
product_value --> res_company : many2one
product_value --> res_currency : many2one
class "res.users" as res_users
product_value --> res_users : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
StockLocation --> account_account : many2one
StockLot --> res_currency : many2one
StockMove --> res_currency : many2one
class "account.analytic.line" as account_analytic_line
StockMove .. account_analytic_line : many2many
class "account.move" as account_move
StockMove --> account_move : many2one
StockQuant --> res_currency : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





