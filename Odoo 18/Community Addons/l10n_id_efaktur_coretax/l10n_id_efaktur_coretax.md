<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indonesia E-faktur (Coretax)

- Version: v18
- Category: community
- Source: odoo/addons/l10n_id_efaktur_coretax
- Dependencies: [[Odoo 18/Community Addons/l10n_id/l10n_id|l10n_id]], [[Odoo 18/Community Addons/l10n_id_efaktur/l10n_id_efaktur|l10n_id_efaktur]]
## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `l10n_id_efaktur_coretax.document`
- `l10n_id_efaktur_coretax.product.code`
- `ProductTemplate`
- `Partner`
- `l10n_id_efaktur_coretax.uom.code`
- `Uom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indonesia E-faktur (Coretax) - Models and Relations
class AccountMove
class AccountMoveLine
class "l10n_id_efaktur_coretax.document" as l10n_id_efaktur_coretax_document
class "l10n_id_efaktur_coretax.product.code" as l10n_id_efaktur_coretax_product_code
class ProductTemplate
class Partner
class "l10n_id_efaktur_coretax.uom.code" as l10n_id_efaktur_coretax_uom_code
class Uom
AccountMove --> l10n_id_efaktur_coretax_document : many2one
class "res.company" as res_company
l10n_id_efaktur_coretax_document --> res_company : many2one
class "account.move" as account_move
l10n_id_efaktur_coretax_document --|> account_move : one2many
class "ir.attachment" as ir_attachment
l10n_id_efaktur_coretax_document --> ir_attachment : many2one
ProductTemplate --> l10n_id_efaktur_coretax_product_code : many2one
Uom --> l10n_id_efaktur_coretax_uom_code : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
