<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders (with Inventory link)

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_purchase_stock_inter_company_rules
- Dependencies: [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[Odoo 18/Enterprise Addons/sale_purchase_inter_company_rules/sale_purchase_inter_company_rules|sale_purchase_inter_company_rules]]

## Summary

Intercompany SO/PO

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `purchase_order`
- `res_company`
- `sale_order`
- `SaleOrderLine`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders (with Inventory link) - Models and Relations
class purchase_order
class res_company
class sale_order
class SaleOrderLine
class StockPicking
class "stock.warehouse" as stock_warehouse
res_company --> stock_warehouse : many2one
class "stock.picking.type" as stock_picking_type
res_company --> stock_picking_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
