<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Peru - Accounting

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_pe
- Dependencies: [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 19/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[Odoo 19/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 19/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 19/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 19/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `AccountTax`
- `L10n_LatamIdentificationType`
- `ResBank`
- `ResCity`
- `l10n_pe.res.city.district`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Peru - Accounting - Models and Relations
class AccountMove
class AccountTax
class L10n_LatamIdentificationType
class ResBank
class ResCity
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
