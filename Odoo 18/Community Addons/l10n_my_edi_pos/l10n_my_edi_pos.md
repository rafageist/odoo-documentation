<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Malaysia - E-invoicing (POS)

- Version: v18
- Category: community
- Source: odoo/addons/l10n_my_edi_pos
- Dependencies: [[Odoo 18/Community Addons/l10n_my_edi_extended/l10n_my_edi_extended|l10n_my_edi_extended]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Consolidated E-invoicing using MyInvois

## XML Artifacts (detected)

- Views: 9
- Actions: 2
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `AccountTax`
- `myinvois.document`
- `MyInvoisDocumentPoS`
- `PosOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Malaysia - E-invoicing (POS) - Models and Relations
class AccountTax
class "myinvois.document" as myinvois_document
class MyInvoisDocumentPoS
class PosOrder
class "res.company" as res_company
myinvois_document --> res_company : many2one
class "res.currency" as res_currency
myinvois_document --> res_currency : many2one
class "ir.attachment" as ir_attachment
myinvois_document --> ir_attachment : many2one
class "account.move" as account_move
myinvois_document .. account_move : many2many
class "pos.order" as pos_order
MyInvoisDocumentPoS .. pos_order : many2many
class "pos.config" as pos_config
MyInvoisDocumentPoS --> pos_config : many2one
PosOrder .. myinvois_document : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
