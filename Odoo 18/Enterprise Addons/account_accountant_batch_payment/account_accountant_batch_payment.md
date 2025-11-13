<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Account Batch Payment Reconciliation

- Version: v18
- Category: enterprise
- Source: enterprise18/account_accountant_batch_payment
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 18/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]

## Summary

Allows using Reconciliation with the Batch Payment feature.

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountBatchPayment`
- `AccountReconcileModel`
- `BankRecWidget`
- `BankRecWidgetLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Batch Payment Reconciliation - Models and Relations
class AccountBatchPayment
class AccountReconcileModel
class BankRecWidget
class BankRecWidgetLine
class "account.batch.payment" as account_batch_payment
BankRecWidget .. account_batch_payment : many2many
BankRecWidgetLine --> account_batch_payment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
