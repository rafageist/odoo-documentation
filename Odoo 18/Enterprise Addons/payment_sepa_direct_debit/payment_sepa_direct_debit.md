<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Payment Provider: Sepa Direct Debit

- Version: v18
- Category: enterprise
- Source: enterprise18/payment_sepa_direct_debit
- Dependencies: [[Odoo 18/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]], [[Odoo 18/Community Addons/account_payment/account_payment|account_payment]], [[Odoo 18/Community Addons/payment_custom/payment_custom|payment_custom]]

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
- `SDDMandate`


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
class SDDMandate
class "sdd.mandate" as sdd_mandate
PaymentToken --> sdd_mandate : many2one
PaymentTransaction --> sdd_mandate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
