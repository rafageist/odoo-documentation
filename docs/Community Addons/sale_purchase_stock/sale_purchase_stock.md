<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# MTO Sale <-> Purchase

- Scope: Community Addons
- Source: odoo/addons/sale_purchase_stock
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[docs/Community Addons/sale_purchase/sale_purchase|sale_purchase]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




