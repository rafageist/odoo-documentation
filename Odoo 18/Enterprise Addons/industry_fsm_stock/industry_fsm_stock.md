<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Field Service Stock

- Version: v18
- Category: enterprise
- Source: enterprise18/industry_fsm_stock
- Dependencies: [[Odoo 18/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Validate stock moves for product added on sales orders through Field Service Management App

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `ProductProduct`
- `ProjectProject`
- `Task`
- `SaleOrder`
- `SaleOrderLine`
- `StockMove`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service Stock - Models and Relations
class ProductProduct
class ProjectProject
class Task
class SaleOrder
class SaleOrderLine
class StockMove
class "stock.lot" as stock_lot
SaleOrderLine --> stock_lot : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
