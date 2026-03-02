<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Point of Sale online payment

- Scope: Community Addons
- Source: odoo/addons/pos_online_payment
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/account_payment/account_payment|account_payment]]

## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountPayment`
- `PaymentTransaction`
- `PosConfig`
- `PosOrder`
- `PosPayment`
- `PosPaymentMethod`
- `PosSession`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Point of Sale online payment - Models and Relations
class AccountPayment
class PaymentTransaction
class PosConfig
class PosOrder
class PosPayment
class PosPaymentMethod
class PosSession
class "pos.order" as pos_order
AccountPayment --> pos_order : many2one
PaymentTransaction --> pos_order : many2one
class "pos.payment.method" as pos_payment_method
PosOrder --> pos_payment_method : many2one
class "account.payment" as account_payment
PosPayment --> account_payment : many2one
class "payment.provider" as payment_provider
PosPaymentMethod .. payment_provider : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





