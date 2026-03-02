<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS Self-Order / Online Payment

- Scope: Community Addons
- Source: odoo/addons/pos_online_payment_self_order
- Dependencies: [[docs/Community Addons/pos_online_payment/pos_online_payment|pos_online_payment]], [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





