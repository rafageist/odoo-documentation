<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Website Payment

- Version: v18
- Category: community
- Source: odoo/addons/website_payment
- Dependencies: [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/account_payment/account_payment|account_payment]], [[Odoo 18/Community Addons/portal/portal|portal]]

## Summary

Payment integration with website

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountPayment`
- `PaymentProvider`
- `PaymentTransaction`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Payment - Models and Relations
class AccountPayment
class PaymentProvider
class PaymentTransaction
class website
PaymentProvider --> website : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
