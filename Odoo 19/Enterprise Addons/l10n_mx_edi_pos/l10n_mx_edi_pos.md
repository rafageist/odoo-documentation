<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Mexican Localization for the Point of Sale

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_mx_edi_pos
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `L10n_Mx_EdiDocument`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosPaymentMethod`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexican Localization for the Point of Sale - Models and Relations
class AccountMove
class AccountMoveLine
class L10n_Mx_EdiDocument
class PosConfig
class PosOrder
class PosOrderLine
class PosPaymentMethod
class ResPartner
class "pos.order" as pos_order
L10n_Mx_EdiDocument .. pos_order : many2many
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
