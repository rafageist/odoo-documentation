<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Payment Provider: Sepa Direct Debit

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/payment_sepa_direct_debit
- Dependencies: [[Odoo 19/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]], [[Odoo 19/Community Addons/account_payment/account_payment|account_payment]], [[Odoo 19/Community Addons/payment_custom/payment_custom|payment_custom]]

## Summary

A payment provider for enabling Sepa Direct Debit in the EU.

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountBankStatementLine`
- `AccountPaymentMethod`
- `PaymentProvider`
- `PaymentToken`
- `PaymentTransaction`
- `ResPartner`
- `SddMandate`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Payment Provider: Sepa Direct Debit - Models and Relations
class AccountBankStatementLine
class AccountPaymentMethod
class PaymentProvider
class PaymentToken
class PaymentTransaction
class ResPartner
class SddMandate
class "sdd.mandate" as sdd_mandate
PaymentToken --> sdd_mandate : many2one
PaymentTransaction --> sdd_mandate : many2one
class "payment.transaction" as payment_transaction
SddMandate --|> payment_transaction : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

