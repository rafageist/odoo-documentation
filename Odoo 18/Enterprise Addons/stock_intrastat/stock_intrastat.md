<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Stock Intrastat

- Version: v18
- Category: enterprise
- Source: enterprise18/stock_intrastat
- Dependencies: [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 18/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Stock Intrastat - Models and Relations
class StockWarehouse
class "res.country" as res_country
StockWarehouse --> res_country : many2one
class "account.intrastat.code" as account_intrastat_code
StockWarehouse --> account_intrastat_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
