<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sale order spreadsheet

- Version: v18
- Category: enterprise
- Source: enterprise18/spreadsheet_sale_management
- Dependencies: [[Odoo 18/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 7
- Access CSV entries: 1

## Detected Models

- `SaleOrder`
- `sale.order.spreadsheet`
- `SaleOrderTemplate`
- `SpreadsheetCellThread`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale order spreadsheet - Models and Relations
class SaleOrder
class "sale.order.spreadsheet" as sale_order_spreadsheet
class SaleOrderTemplate
class SpreadsheetCellThread
SaleOrder --> sale_order_spreadsheet : many2one
SaleOrder --|> sale_order_spreadsheet : one2many
SaleOrder --> sale_order_spreadsheet : many2one
class "res.company" as res_company
sale_order_spreadsheet --> res_company : many2one
class "sale.order" as sale_order
sale_order_spreadsheet --> sale_order : many2one
SaleOrderTemplate --> sale_order_spreadsheet : many2one
SpreadsheetCellThread --> sale_order_spreadsheet : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
