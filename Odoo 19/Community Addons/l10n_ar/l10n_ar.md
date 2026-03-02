<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Argentina - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ar
- Dependencies: [[Odoo 19/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 19/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 19/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 20
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
- `L10n_LatamDocumentType`
- `L10n_LatamIdentificationType`
- `ResCompany`
- `ResCountry`
- `ResCurrency`
- `ResPartner`
- `ResPartnerBank`
- `UomUom`

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
class L10n_LatamDocumentType
class L10n_LatamIdentificationType
class ResCompany
class ResCountry
class ResCurrency
class ResPartner
class ResPartnerBank
class UomUom
AccountFiscalPosition .. l10n_ar_afip_responsibility_type : many2many
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
AccountJournal --> res_partner : many2one
AccountMove --> l10n_ar_afip_responsibility_type : many2one
ResPartner --> l10n_ar_afip_responsibility_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


