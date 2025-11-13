<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indian - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_in
- Dependencies: [[Odoo 18/Community Addons/account_tax_python/account_tax_python|account_tax_python]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/iap/iap|iap]]
## XML Artifacts (detected)

- Views: 15
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `ResCompany`
- `IapAccount`
- `l10n_in.port.code`
- `ProductTemplate`
- `CountryState`
- `ResPartner`
- `UoM`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - Accounting - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class ResCompany
class IapAccount
class "l10n_in.port.code" as l10n_in_port_code
class ProductTemplate
class CountryState
class ResPartner
class UoM
class "res.country.state" as res_country_state
AccountMove --> res_country_state : many2one
AccountMove --> l10n_in_port_code : many2one
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
l10n_in_port_code --> res_country_state : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
