<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Field Service Stock

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/industry_fsm_stock
- Dependencies: [[Odoo 19/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Validate stock moves for product added on sales orders through Field Service Management App

## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `ProductProduct`
- `ProjectProject`
- `ProjectTask`
- `SaleOrder`
- `SaleOrderLine`
- `StockMove`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service Stock - Models and Relations
class ProductProduct
class ProjectProject
class ProjectTask
class SaleOrder
class SaleOrderLine
class StockMove
class "stock.lot" as stock_lot
SaleOrderLine --> stock_lot : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

