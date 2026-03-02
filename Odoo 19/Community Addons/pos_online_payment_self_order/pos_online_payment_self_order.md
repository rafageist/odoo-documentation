<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# POS Self-Order / Online Payment

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/pos_online_payment_self_order
- Dependencies: [[Odoo 19/Community Addons/pos_online_payment/pos_online_payment|pos_online_payment]], [[Odoo 19/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

## Summary

Support online payment in self-order

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PaymentTransaction`
- `PosConfig`
- `PosOrder`
- `PosPaymentMethod`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS Self-Order / Online Payment - Models and Relations
class PaymentTransaction
class PosConfig
class PosOrder
class PosPaymentMethod
class "pos.payment.method" as pos_payment_method
PosConfig --> pos_payment_method : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


