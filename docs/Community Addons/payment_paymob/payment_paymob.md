<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Payment Provider: Paymob

- Scope: Community Addons
- Source: odoo/addons/payment_paymob
- Dependencies: [[docs/Community Addons/payment/payment|payment]]

## Summary

An Egyptian payment provider for the Middle East.

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PaymentProvider`
- `PaymentTransaction`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Payment Provider: Paymob - Models and Relations
class PaymentProvider
class PaymentTransaction
class "res.country" as res_country
PaymentProvider --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





