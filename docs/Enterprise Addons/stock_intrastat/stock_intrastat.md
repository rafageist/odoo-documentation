<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Stock Intrastat

- Scope: Enterprise Addons
- Source: enterprise/stock_intrastat
- Dependencies: [[docs/Community Addons/stock_account/stock_account|stock_account]], [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]

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
!include ../../../templates/DiagramStyles.puml
title Stock Intrastat - Models and Relations
class StockWarehouse
class "res.country" as res_country
StockWarehouse --> res_country : many2one
class "account.intrastat.code" as account_intrastat_code
StockWarehouse --> account_intrastat_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



