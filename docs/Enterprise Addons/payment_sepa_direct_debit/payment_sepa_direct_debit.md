<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payment Provider: Sepa Direct Debit

- Scope: Enterprise Addons
- Source: enterprise/payment_sepa_direct_debit
- Dependencies: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/payment_custom/payment_custom|payment_custom]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




