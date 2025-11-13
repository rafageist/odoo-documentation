<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# MTO Sale <-> Purchase

- Version: v18
- Category: community
- Source: odoo/addons/sale_purchase_stock
- Dependencies: [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[Odoo 18/Community Addons/sale_purchase/sale_purchase|sale_purchase]]

## Summary

SO/PO relation in case of MTO

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `PurchaseOrderLine`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MTO Sale <-> Purchase - Models and Relations
class PurchaseOrder
class PurchaseOrderLine
class SaleOrder
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
