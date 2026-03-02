<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Scope: Enterprise Addons
- Source: enterprise/account_inter_company_rules
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



