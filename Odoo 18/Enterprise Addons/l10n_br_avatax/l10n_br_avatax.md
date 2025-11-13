<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Avatax Brazil

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_br_avatax
- Dependencies: [[Odoo 18/Community Addons/iap/iap|iap]], [[Odoo 18/Community Addons/l10n_br/l10n_br|l10n_br]], [[Odoo 18/Enterprise Addons/account_external_tax/account_external_tax|account_external_tax]]
## XML Artifacts (detected)

- Views: 11
- Actions: 3
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 7

## Detected Models

- `AccountFiscalPosition`
- `AccountMove`
- `AccountTax`
- `l10n_br.cnae.code`
- `l10n_br.ncm.code`
- `l10n_br.operation.type`
- `l10n_br.service.code`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Avatax Brazil - Models and Relations
class AccountFiscalPosition
class AccountMove
class AccountTax
class "l10n_br.cnae.code" as l10n_br_cnae_code
class "l10n_br.ncm.code" as l10n_br_ncm_code
class "l10n_br.operation.type" as l10n_br_operation_type
class "l10n_br.service.code" as l10n_br_service_code
class ProductTemplate
class ResCompany
class ResPartner
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
