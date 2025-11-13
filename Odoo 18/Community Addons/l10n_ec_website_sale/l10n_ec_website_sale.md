<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Ecuadorian Website

- Version: v18
- Category: community
- Source: odoo/addons/l10n_ec_website_sale
- Dependencies: [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 18/Community Addons/l10n_ec/l10n_ec|l10n_ec]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PaymentMethod`
- `SaleOrder`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Ecuadorian Website - Models and Relations
class PaymentMethod
class SaleOrder
class Website
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
PaymentMethod --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
