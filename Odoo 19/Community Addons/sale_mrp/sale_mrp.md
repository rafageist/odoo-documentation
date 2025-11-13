<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales and MRP Management

- Version: v19
- Category: community
- Source: odoo19/addons/sale_mrp
- Dependencies: [[Odoo 19/Community Addons/mrp/mrp|mrp]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `AccountMoveLine`
- `MrpBom`
- `MrpProduction`
- `SaleOrder`
- `SaleOrderLine`
- `StockMoveLine`
- `StockRule`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales and MRP Management - Models and Relations
class AccountMoveLine
class MrpBom
class MrpProduction
class SaleOrder
class SaleOrderLine
class StockMoveLine
class StockRule
class "sale.order.line" as sale_order_line
MrpProduction --> sale_order_line : many2one
class "mrp.production" as mrp_production
SaleOrder .. mrp_production : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
