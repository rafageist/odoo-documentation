<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Budget Management

- Scope: Enterprise Addons
- Source: enterprise/account_budget
- Dependencies: [[docs/Enterprise Addons/accountant/accountant|accountant]]

## XML Artifacts (detected)

- Views: 15
- Actions: 4
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 7

## Detected Models

- `AccountAnalyticAccount`
- `budget.analytic`
- `budget.line`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Budget Management - Models and Relations
class AccountAnalyticAccount
class "budget.analytic" as budget_analytic
class "budget.line" as budget_line
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
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



