<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sale Purchase

- Version: v18
- Category: community
- Source: odoo/addons/sale_purchase
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/purchase/purchase|purchase]]

## Summary

Sale based on service outsourcing.

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductTemplate`
- `PurchaseOrder`
- `PurchaseOrderLine`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale Purchase - Models and Relations
class ProductTemplate
class PurchaseOrder
class PurchaseOrderLine
class SaleOrder
class SaleOrderLine
class "sale.order.line" as sale_order_line
PurchaseOrderLine --> sale_order_line : many2one
class "purchase.order.line" as purchase_order_line
SaleOrderLine --|> purchase_order_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
