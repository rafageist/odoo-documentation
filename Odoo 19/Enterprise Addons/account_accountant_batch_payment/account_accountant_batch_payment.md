<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Account Batch Payment Reconciliation

- Version: v19
- Category: enterprise
- Source: enterprise19/account_accountant_batch_payment
- Dependencies: [[Odoo 19/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 19/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]

## Summary

Allows using Reconciliation with the Batch Payment feature.

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `account.bank.statement.line`
- `AccountBatchPayment`
- `account.move.line`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Batch Payment Reconciliation - Models and Relations
class "account.bank.statement.line" as account_bank_statement_line
class AccountBatchPayment
class "account.move.line" as account_move_line
class "account.payment" as account_payment
account_move_line .. account_payment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
