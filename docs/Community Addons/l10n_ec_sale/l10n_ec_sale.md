<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Ecuador - Sale

- Scope: Community Addons
- Source: odoo/addons/l10n_ec_sale
- Dependencies: [[docs/Community Addons/l10n_ec/l10n_ec|l10n_ec]], [[docs/Community Addons/sale/sale|sale]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PaymentMethod`
- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Ecuador - Sale - Models and Relations
class PaymentMethod
class SaleOrder
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
PaymentMethod --> l10n_ec_sri_payment : many2one
SaleOrder --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





