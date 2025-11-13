<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Greece - myDATA

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_gr_edi
- Dependencies: [[Odoo 19/Community Addons/l10n_gr/l10n_gr|l10n_gr]]

## Summary

Connect to myDATA API implementation for Greece

## XML Artifacts (detected)

- Views: 11
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountFiscalPosition`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `l10n_gr_edi.document`
- `l10n_gr_edi.preferred_classification`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Greece - myDATA - Models and Relations
class AccountFiscalPosition
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_gr_edi.document" as l10n_gr_edi_document
class "l10n_gr_edi.preferred_classification" as l10n_gr_edi_preferred_classification
class ProductTemplate
class ResCompany
class ResPartner
AccountFiscalPosition --|> l10n_gr_edi_preferred_classification : one2many
AccountMove --|> l10n_gr_edi_document : one2many
class "account.move" as account_move
AccountMove --> account_move : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
l10n_gr_edi_document --> account_move : many2one
l10n_gr_edi_document --> ir_attachment : many2one
class "product.template" as product_template
l10n_gr_edi_preferred_classification --> product_template : many2one
class "account.fiscal.position" as account_fiscal_position
l10n_gr_edi_preferred_classification --> account_fiscal_position : many2one
ProductTemplate --|> l10n_gr_edi_preferred_classification : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
