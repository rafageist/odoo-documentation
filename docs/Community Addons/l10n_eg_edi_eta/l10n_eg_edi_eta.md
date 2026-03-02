<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Egypt E-Invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_eg_edi_eta
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/l10n_eg/l10n_eg|l10n_eg]]

## Summary


            Egypt Tax Authority Invoice Integration
        

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `AccountEdiFormat`
- `AccountJournal`
- `AccountMove`
- `l10n_eg_edi.activity.type`
- `l10n_eg_edi.thumb.drive`
- `ProductTemplate`
- `ProductProduct`
- `ResCompany`
- `ResCurrencyRate`
- `ResPartner`
- `l10n_eg_edi.uom.code`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Egypt E-Invoicing - Models and Relations
class AccountEdiFormat
class AccountJournal
class AccountMove
class "l10n_eg_edi.activity.type" as l10n_eg_edi_activity_type
class "l10n_eg_edi.thumb.drive" as l10n_eg_edi_thumb_drive
class ProductTemplate
class ProductProduct
class ResCompany
class ResCurrencyRate
class ResPartner
class "l10n_eg_edi.uom.code" as l10n_eg_edi_uom_code
class UomUom
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
AccountJournal --> l10n_eg_edi_activity_type : many2one
class "res.users" as res_users
l10n_eg_edi_thumb_drive --> res_users : many2one
class "res.company" as res_company
l10n_eg_edi_thumb_drive --> res_company : many2one
UomUom --> l10n_eg_edi_uom_code : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





