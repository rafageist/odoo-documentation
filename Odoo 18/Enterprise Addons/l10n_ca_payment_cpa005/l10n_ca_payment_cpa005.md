<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# CPA005 Payments

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ca_payment_cpa005
- Dependencies: [[Odoo 18/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 18/Community Addons/l10n_ca/l10n_ca|l10n_ca]]

## Summary

Export payments as CPA 005 AFT files

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `l10n_ca_cpa005.transaction.code`
- `ResCompany`
- `ResPartnerBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title CPA005 Payments - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class "l10n_ca_cpa005.transaction.code" as l10n_ca_cpa005_transaction_code
class ResCompany
class ResPartnerBank
class "ir.sequence" as ir_sequence
AccountJournal --> ir_sequence : many2one
AccountPayment --> l10n_ca_cpa005_transaction_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
