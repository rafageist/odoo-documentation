<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Website Payment

- Version: v19
- Category: community
- Source: odoo19/addons/website_payment
- Dependencies: [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Community Addons/account_payment/account_payment|account_payment]], [[Odoo 19/Community Addons/portal/portal|portal]]

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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
