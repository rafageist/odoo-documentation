<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/account_inter_company_rules
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

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
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders and Invoices - Models and Relations
class AccountMove
class AccountMoveLine
class ResCompany
class "account.move" as account_move
AccountMove --> account_move : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
class "res.users" as res_users
ResCompany --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

