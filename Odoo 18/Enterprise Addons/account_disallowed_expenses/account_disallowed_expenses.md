<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Disallowed Expenses

- Version: v18
- Category: enterprise
- Source: enterprise18/account_disallowed_expenses
- Dependencies: [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]

## Summary

Manage disallowed expenses

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountAccount`
- `account.disallowed.expenses.category`
- `account.disallowed.expenses.rate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Disallowed Expenses - Models and Relations
class AccountAccount
class "account.disallowed.expenses.category" as account_disallowed_expenses_category
class "account.disallowed.expenses.rate" as account_disallowed_expenses_rate
AccountAccount --> account_disallowed_expenses_category : many2one
account_disallowed_expenses_category --|> account_disallowed_expenses_rate : one2many
class "res.company" as res_company
account_disallowed_expenses_category --> res_company : many2one
class "account.account" as account_account
account_disallowed_expenses_category --|> account_account : one2many
account_disallowed_expenses_rate --> account_disallowed_expenses_category : many2one
account_disallowed_expenses_rate --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
