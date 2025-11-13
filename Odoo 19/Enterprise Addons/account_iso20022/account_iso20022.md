<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# SEPA Credit Transfer / ISO20022

- Version: v19
- Category: enterprise
- Source: enterprise19/account_iso20022
- Dependencies: [[Odoo 19/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]]

## Summary

Export payments as SEPA Credit Transfer or ISO20022 files

## XML Artifacts (detected)

- Views: 11
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountBankStatementLine`
- `AccountBatchPayment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title SEPA Credit Transfer / ISO20022 - Models and Relations
class AccountBankStatementLine
class AccountBatchPayment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class ResCompany
class ResPartner
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
