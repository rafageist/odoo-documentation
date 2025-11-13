<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Intrastat Reports

- Version: v19
- Category: enterprise
- Source: enterprise19/account_intrastat
- Dependencies: [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 22
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `account.intrastat.code`
- `AccountMove`
- `AccountMoveLine`
- `AccountReturnType`
- `AccountReturn`
- `ProductTemplate`
- `ProductProduct`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Intrastat Reports - Models and Relations
class "account.intrastat.code" as account_intrastat_code
class AccountMove
class AccountMoveLine
class AccountReturnType
class AccountReturn
class ProductTemplate
class ProductProduct
class ResCompany
class "res.country" as res_country
account_intrastat_code --> res_country : many2one
AccountMove --> account_intrastat_code : many2one
AccountMove --> res_country : many2one
AccountMoveLine --> account_intrastat_code : many2one
AccountMoveLine --> res_country : many2one
ProductTemplate --> account_intrastat_code : many2one
ProductTemplate --> res_country : many2one
ProductTemplate .. account_intrastat_code : many2many
ProductProduct --> account_intrastat_code : many2one
ProductProduct --> res_country : many2one
ResCompany --> account_intrastat_code : many2one
ResCompany --> account_intrastat_code : many2one
ResCompany --> account_intrastat_code : many2one
ResCompany --> account_intrastat_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
