<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders (with Inventory link)

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_purchase_stock_inter_company_rules
- Dependencies: [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[Odoo 19/Enterprise Addons/sale_purchase_inter_company_rules/sale_purchase_inter_company_rules|sale_purchase_inter_company_rules]]

## Summary

Intercompany SO/PO

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `ResCompany`
- `SaleOrder`
- `SaleOrderLine`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders (with Inventory link) - Models and Relations
class PurchaseOrder
class ResCompany
class SaleOrder
class SaleOrderLine
class StockPicking
class "stock.warehouse" as stock_warehouse
ResCompany --> stock_warehouse : many2one
class "stock.picking.type" as stock_picking_type
ResCompany --> stock_picking_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
