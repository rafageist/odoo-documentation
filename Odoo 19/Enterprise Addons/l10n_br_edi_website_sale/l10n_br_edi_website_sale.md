<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Brazilian Accounting EDI for eCommerce

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_br_edi_website_sale
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_br_edi_sale/l10n_br_edi_sale|l10n_br_edi_sale]], [[Odoo 19/Enterprise Addons/website_sale_external_tax/website_sale_external_tax|website_sale_external_tax]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI for eCommerce - Models and Relations
class DeliveryCarrier
class SaleOrder
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
