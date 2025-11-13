<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Budget Management

- Version: v18
- Category: enterprise
- Source: enterprise18/account_budget
- Dependencies: [[Odoo 18/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 18/Community Addons/purchase/purchase|purchase]]
## XML Artifacts (detected)

- Views: 16
- Actions: 4
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 7

## Detected Models

- `AccountAnalyticAccount`
- `budget.analytic`
- `budget.line`
- `PurchaseOrder`
- `PurchaseOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Budget Management - Models and Relations
class AccountAnalyticAccount
class "budget.analytic" as budget_analytic
class "budget.line" as budget_line
class PurchaseOrder
class PurchaseOrderLine
AccountAnalyticAccount --|> budget_line : one2many
budget_analytic --> budget_analytic : many2one
budget_analytic --|> budget_analytic : one2many
class "res.users" as res_users
budget_analytic --> res_users : many2one
budget_analytic --|> budget_line : one2many
class "res.company" as res_company
budget_analytic --> res_company : many2one
budget_line --> budget_analytic : many2one
class "res.currency" as res_currency
budget_line --> res_currency : many2one
budget_line --> res_company : many2one
PurchaseOrderLine --|> budget_line : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
