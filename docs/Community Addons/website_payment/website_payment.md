<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Website Payment

- Scope: Community Addons
- Source: odoo/addons/website_payment
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/portal/portal|portal]]

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
!include ../../../templates/DiagramStyles.puml
title Website Payment - Models and Relations
class AccountPayment
class PaymentProvider
class PaymentTransaction
class website
PaymentProvider --> website : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



