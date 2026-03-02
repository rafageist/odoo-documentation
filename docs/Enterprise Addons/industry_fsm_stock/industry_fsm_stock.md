<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service Stock

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_stock
- Dependencies: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



