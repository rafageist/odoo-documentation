<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Payment Provider: Paymob

- Version: v19
- Category: community
- Source: odoo19/addons/payment_paymob
- Dependencies: [[Odoo 19/Community Addons/payment/payment|payment]]

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
!include ../../../Templates/DiagramStyles.puml
title Payment Provider: Paymob - Models and Relations
class PaymentProvider
class PaymentTransaction
class "res.country" as res_country
PaymentProvider --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
