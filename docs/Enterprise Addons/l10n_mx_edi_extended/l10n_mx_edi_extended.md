<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# EDI for Mexico (Advanced Features)

- Scope: Enterprise Addons
- Source: enterprise/l10n_mx_edi_extended
- Dependencies: [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]]

## XML Artifacts (detected)

- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `L10n_Mx_EdiDocument`
- `l10n_mx_edi.res.locality`
- `l10n_mx_edi.tariff.fraction`
- `ProductTemplate`
- `ResCity`
- `ResCompany`
- `ResPartner`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title EDI for Mexico (Advanced Features) - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class L10n_Mx_EdiDocument
class "l10n_mx_edi.res.locality" as l10n_mx_edi_res_locality
class "l10n_mx_edi.tariff.fraction" as l10n_mx_edi_tariff_fraction
class ProductTemplate
class ResCity
class ResCompany
class ResPartner
class UomUom
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
class "uom.uom" as uom_uom
AccountMoveLine --> uom_uom : many2one
class "res.country" as res_country
l10n_mx_edi_res_locality --> res_country : many2one
class "res.country.state" as res_country_state
l10n_mx_edi_res_locality --> res_country_state : many2one
ProductTemplate --> l10n_mx_edi_tariff_fraction : many2one
ProductTemplate --> uom_uom : many2one
ResCompany --> l10n_mx_edi_res_locality : many2one
ResPartner --> l10n_mx_edi_res_locality : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



