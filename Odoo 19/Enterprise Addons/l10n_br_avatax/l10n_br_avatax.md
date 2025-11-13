<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Avatax Brazil

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_br_avatax
- Dependencies: [[Odoo 19/Community Addons/iap/iap|iap]], [[Odoo 19/Community Addons/l10n_br/l10n_br|l10n_br]], [[Odoo 19/Enterprise Addons/account_external_tax/account_external_tax|account_external_tax]]
## XML Artifacts (detected)

- Views: 16
- Actions: 4
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 8

## Detected Models

- `AccountFiscalPosition`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `l10n_br.cnae.code`
- `l10n_br.ncm.code`
- `l10n_br.operation.type`
- `l10n_br.service.code`
- `ProductProduct`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Avatax Brazil - Models and Relations
class AccountFiscalPosition
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_br.cnae.code" as l10n_br_cnae_code
class "l10n_br.ncm.code" as l10n_br_ncm_code
class "l10n_br.operation.type" as l10n_br_operation_type
class "l10n_br.service.code" as l10n_br_service_code
class ProductProduct
class ProductTemplate
class ResCompany
class ResPartner
AccountMoveLine --> l10n_br_operation_type : many2one
l10n_br_ncm_code --> l10n_br_cnae_code : many2one
class "res.city" as res_city
l10n_br_service_code --> res_city : many2one
class "res.company" as res_company
l10n_br_service_code --> res_company : many2one
ProductTemplate --> l10n_br_ncm_code : many2one
ProductTemplate --> l10n_br_service_code : many2one
ProductTemplate .. l10n_br_service_code : many2many
ProductTemplate --> res_city : many2one
ResCompany --> l10n_br_cnae_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
