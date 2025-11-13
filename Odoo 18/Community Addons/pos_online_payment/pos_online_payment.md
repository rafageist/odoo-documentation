<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Point of Sale online payment

- Version: v18
- Category: community
- Source: odoo/addons/pos_online_payment
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Community Addons/account_payment/account_payment|account_payment]]
## XML Artifacts (detected)

- Views: 5
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
