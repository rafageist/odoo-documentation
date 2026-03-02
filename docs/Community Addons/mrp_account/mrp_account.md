<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Accounting - MRP

- Scope: Community Addons
- Source: odoo/addons/mrp_account
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Analytic accounting in Manufacturing

## XML Artifacts (detected)

- Views: 9
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
- `mrp.workcenter`
- `MrpWorkcenterProductivity`
- `MrpWorkorder`
- `ProductTemplate`
- `ProductProduct`
- `ProductCategory`
- `StockMove`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Accounting - MRP - Models and Relations
class AccountMove
class AccountMoveLine
class AccountAnalyticAccount
class AccountAnalyticLine
class AccountAnalyticApplicability
class MrpProduction
class "mrp.workcenter" as mrp_workcenter
class MrpWorkcenterProductivity
class MrpWorkorder
class ProductTemplate
class ProductProduct
class ProductCategory
class StockMove
class "mrp.production" as mrp_production
AccountMove .. mrp_production : many2many
AccountAnalyticAccount .. mrp_production : many2many
class "mrp.bom" as mrp_bom
AccountAnalyticAccount .. mrp_bom : many2many
AccountAnalyticAccount .. mrp_workcenter : many2many
class "account.move" as account_move
MrpProduction .. account_move : many2many
class "account.analytic.account" as account_analytic_account
mrp_workcenter .. account_analytic_account : many2many
class "account.account" as account_account
mrp_workcenter --> account_account : many2one
class "account.move.line" as account_move_line
MrpWorkcenterProductivity --> account_move_line : many2one
class "account.analytic.line" as account_analytic_line
MrpWorkorder .. account_analytic_line : many2many
MrpWorkorder .. account_analytic_line : many2many
ProductCategory --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





