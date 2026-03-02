<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Batch Payment Reconciliation

- Scope: Enterprise Addons
- Source: enterprise/account_accountant_batch_payment
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]

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
!include ../../../templates/DiagramStyles.puml
title Account Batch Payment Reconciliation - Models and Relations
class "account.bank.statement.line" as account_bank_statement_line
class AccountBatchPayment
class "account.move.line" as account_move_line
class "account.payment" as account_payment
account_move_line .. account_payment : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



