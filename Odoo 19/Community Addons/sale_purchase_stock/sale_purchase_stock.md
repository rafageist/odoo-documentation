<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# MTO Sale <-> Purchase

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/sale_purchase_stock
- Dependencies: [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[Odoo 19/Community Addons/sale_purchase/sale_purchase|sale_purchase]]

## Summary

SO/PO relation in case of MTO

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `PurchaseOrderLine`
- `SaleOrder`
- `StockMove`
- `StockRule`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MTO Sale <-> Purchase - Models and Relations
class PurchaseOrder
class PurchaseOrderLine
class SaleOrder
class StockMove
class StockRule
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

