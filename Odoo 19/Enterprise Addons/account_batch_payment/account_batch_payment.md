<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Batch Payment

- Version: v19
- Category: enterprise
- Source: enterprise19/account_batch_payment
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 12
- Actions: 4
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `account.batch.payment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Batch Payment - Models and Relations
class "account.batch.payment" as account_batch_payment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class "account.journal" as account_journal
account_batch_payment --> account_journal : many2one
class "res.company" as res_company
account_batch_payment --> res_company : many2one
class "account.payment" as account_payment
account_batch_payment --|> account_payment : one2many
class "res.currency" as res_currency
account_batch_payment --> res_currency : many2one
class "account.payment.method" as account_payment_method
account_batch_payment --> account_payment_method : many2one
account_batch_payment .. account_payment_method : many2many
AccountPayment --> account_batch_payment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
