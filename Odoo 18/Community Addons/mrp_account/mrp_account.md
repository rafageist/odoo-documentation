<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Accounting - MRP

- Version: v18
- Category: community
- Source: odoo/addons/mrp_account
- Dependencies: [[Odoo 18/Community Addons/mrp/mrp|mrp]], [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Analytic accounting in Manufacturing

## XML Artifacts (detected)

- Views: 10
- Actions: 4
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountAnalyticAccount`
- `AccountAnalyticLine`
- `AccountAnalyticApplicability`
- `MrpProduction`
- `MrpRoutingWorkcenter`
- `mrp.workcenter`
- `mrp.workcenter.productivity`
- `MrpWorkorder`
- `product.template`
- `product.product`
- `ProductCategory`
- `StockMove`
- `StockValuationLayer`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Accounting - MRP - Models and Relations
class AccountMove
class AccountMoveLine
class AccountAnalyticAccount
class AccountAnalyticLine
class AccountAnalyticApplicability
class MrpProduction
class MrpRoutingWorkcenter
class "mrp.workcenter" as mrp_workcenter
class "mrp.workcenter.productivity" as mrp_workcenter_productivity
class MrpWorkorder
class "product.template" as product_template
class "product.product" as product_product
class ProductCategory
class StockMove
class StockValuationLayer
class "mrp.production" as mrp_production
AccountMove .. mrp_production : many2many
AccountAnalyticAccount .. mrp_production : many2many
class "mrp.bom" as mrp_bom
AccountAnalyticAccount .. mrp_bom : many2many
AccountAnalyticAccount .. mrp_workcenter : many2many
class "account.analytic.account" as account_analytic_account
mrp_workcenter .. account_analytic_account : many2many
class "account.account" as account_account
mrp_workcenter --> account_account : many2one
class "account.move.line" as account_move_line
mrp_workcenter_productivity --> account_move_line : many2one
class "account.analytic.line" as account_analytic_line
MrpWorkorder .. account_analytic_line : many2many
MrpWorkorder .. account_analytic_line : many2many
ProductCategory --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
