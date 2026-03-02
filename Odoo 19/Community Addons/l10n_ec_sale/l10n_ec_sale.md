<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Ecuador - Sale

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ec_sale
- Dependencies: [[Odoo 19/Community Addons/l10n_ec/l10n_ec|l10n_ec]], [[Odoo 19/Community Addons/sale/sale|sale]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


