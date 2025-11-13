<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Version: v18
- Category: enterprise
- Source: enterprise18/account_inter_company_rules
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]

## Summary

Intercompany SO/PO/INV rules

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `res_company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders and Invoices - Models and Relations
class AccountMove
class AccountMoveLine
class res_company
class "account.move" as account_move
AccountMove --> account_move : many2one
class "account.journal" as account_journal
res_company --> account_journal : many2one
class "res.users" as res_users
res_company --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
