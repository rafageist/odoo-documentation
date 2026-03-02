<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Payment Provider: Mercado Pago

- Scope: Community Addons
- Source: odoo/addons/payment_mercado_pago
- Dependencies: [[docs/Community Addons/payment/payment|payment]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





