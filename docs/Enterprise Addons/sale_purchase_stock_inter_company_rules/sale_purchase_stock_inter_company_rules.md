
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders (with Inventory link)

- Scope: Enterprise Addons
- Source: enterprise/sale_purchase_stock_inter_company_rules
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[docs/Enterprise Addons/sale_purchase_inter_company_rules/sale_purchase_inter_company_rules|sale_purchase_inter_company_rules]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


