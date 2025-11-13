<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Intrastat Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/account_intrastat
- Dependencies: [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 23
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `account.intrastat.code`
- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `ProductProduct`
- `ResCompany`
- `ResCountry`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Intrastat Reports - Models and Relations
class "account.intrastat.code" as account_intrastat_code
class AccountMove
class AccountMoveLine
class ProductTemplate
class ProductProduct
class ResCompany
class ResCountry
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
