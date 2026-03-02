<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Brazilian Accounting EDI for eCommerce

- Scope: Enterprise Addons
- Source: enterprise/l10n_br_edi_website_sale
- Dependencies: [[docs/Enterprise Addons/l10n_br_edi_sale/l10n_br_edi_sale|l10n_br_edi_sale]], [[docs/Enterprise Addons/website_sale_external_tax/website_sale_external_tax|website_sale_external_tax]]

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
!include ../../../templates/DiagramStyles.puml
title Brazilian Accounting EDI for eCommerce - Models and Relations
class DeliveryCarrier
class SaleOrder
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



