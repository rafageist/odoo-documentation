<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Peru - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_pe
- Dependencies: [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[Odoo 18/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 18/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 18/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountTax`
- `L10nLatamIdentificationType`
- `ResBank`
- `City`
- `l10n_pe.res.city.district`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Peru - Accounting - Models and Relations
class AccountMove
class AccountTax
class L10nLatamIdentificationType
class ResBank
class City
class "l10n_pe.res.city.district" as l10n_pe_res_city_district
class ResCompany
class ResPartner
class "res.city" as res_city
l10n_pe_res_city_district --> res_city : many2one
ResPartner --> l10n_pe_res_city_district : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
