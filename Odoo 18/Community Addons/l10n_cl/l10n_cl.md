<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Chile - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_cl
- Dependencies: [[Odoo 18/Community Addons/contacts/contacts|contacts]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 18/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 18/Community Addons/uom/uom|uom]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 12
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `L10nLatamDocumentType`
- `ResCompany`
- `res.country`
- `res.currency`
- `res.partner`
- `res.bank`
- `UomUom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Chile - Accounting - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class L10nLatamDocumentType
class ResCompany
class "res.country" as res_country
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.bank" as res_bank
class UomUom
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
