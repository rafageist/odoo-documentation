<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Argentina - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_ar
- Dependencies: [[Odoo 18/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 18/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 21
- Actions: 4
- Menus: 6
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountFiscalPosition`
- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountTaxGroup`
- `l10n_ar.afip.responsibility.type`
- `L10nLatamDocumentType`
- `L10nLatamIdentificationType`
- `ResCompany`
- `ResCountry`
- `ResCurrency`
- `ResPartner`
- `ResPartnerBank`
- `Uom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Argentina - Accounting - Models and Relations
class AccountFiscalPosition
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountTaxGroup
class "l10n_ar.afip.responsibility.type" as l10n_ar_afip_responsibility_type
class L10nLatamDocumentType
class L10nLatamIdentificationType
class ResCompany
class ResCountry
class ResCurrency
class ResPartner
class ResPartnerBank
class Uom
AccountFiscalPosition .. l10n_ar_afip_responsibility_type : many2many
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
AccountJournal --> res_partner : many2one
AccountMove --> l10n_ar_afip_responsibility_type : many2one
ResPartner --> l10n_ar_afip_responsibility_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
