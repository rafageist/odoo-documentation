<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Mexican Localization for the Point of Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_mx_edi_pos
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `L10nMxEdiDocument`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosPaymentMethod`
- `PosSession`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexican Localization for the Point of Sale - Models and Relations
class AccountMove
class L10nMxEdiDocument
class PosConfig
class PosOrder
class PosOrderLine
class PosPaymentMethod
class PosSession
class ResPartner
class "pos.order" as pos_order
L10nMxEdiDocument .. pos_order : many2many
class "l10n_mx_edi.document" as l10n_mx_edi_document
PosOrder .. l10n_mx_edi_document : many2many
class "ir.attachment" as ir_attachment
PosOrder --> ir_attachment : many2one
class "l10n_mx_edi.payment.method" as l10n_mx_edi_payment_method
PosOrder --> l10n_mx_edi_payment_method : many2one
PosPaymentMethod --> l10n_mx_edi_payment_method : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
