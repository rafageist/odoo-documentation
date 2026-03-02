<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Payment Provider: Mercado Pago

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/payment_mercado_pago
- Dependencies: [[Odoo 19/Community Addons/payment/payment|payment]]

## Summary

A payment provider covering several countries in Latin America.

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PaymentProvider`
- `PaymentToken`
- `PaymentTransaction`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Payment Provider: Mercado Pago - Models and Relations
class PaymentProvider
class PaymentToken
class PaymentTransaction
class "res.country" as res_country
PaymentProvider --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


