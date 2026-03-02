<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Payment - Account

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/account_payment
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/payment/payment|payment]]

## Summary

Enable customers to pay invoices on the portal and post payments when transactions are processed.

## XML Artifacts (detected)

- Views: 9
- Actions: 1
- Menus: 4
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountPayment`
- `AccountPaymentMethod`
- `AccountPaymentMethodLine`
- `PaymentProvider`
- `PaymentTransaction`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Payment - Account - Models and Relations
class AccountJournal
class AccountMove
class AccountPayment
class AccountPaymentMethod
class AccountPaymentMethodLine
class PaymentProvider
class PaymentTransaction
class "payment.transaction" as payment_transaction
AccountMove .. payment_transaction : many2many
AccountMove .. payment_transaction : many2many
AccountPayment --> payment_transaction : many2one
class "payment.token" as payment_token
AccountPayment --> payment_token : many2one
AccountPayment .. payment_token : many2many
class "account.payment" as account_payment
AccountPayment --> account_payment : many2one
class "payment.provider" as payment_provider
AccountPaymentMethodLine --> payment_provider : many2one
class "account.journal" as account_journal
PaymentProvider --> account_journal : many2one
PaymentTransaction --> account_payment : many2one
class "account.move" as account_move
PaymentTransaction .. account_move : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


