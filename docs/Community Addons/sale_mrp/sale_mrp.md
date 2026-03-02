<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales and MRP Management

- Scope: Community Addons
- Source: odoo/addons/sale_mrp
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




