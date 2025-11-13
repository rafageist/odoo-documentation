<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Purchase Requisition Stock

- Version: v18
- Category: community
- Source: odoo/addons/purchase_requisition_stock
- Dependencies: [[Odoo 18/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]], [[Odoo 18/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `PurchaseOrder`
- `PurchaseOrderLine`
- `PurchaseRequisition`
- `PurchaseRequisitionLine`
- `StockRule`
- `StockMove`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase Requisition Stock - Models and Relations
class PurchaseOrder
class PurchaseOrderLine
class PurchaseRequisition
class PurchaseRequisitionLine
class StockRule
class StockMove
class "stock.warehouse" as stock_warehouse
PurchaseRequisition --> stock_warehouse : many2one
class "stock.picking.type" as stock_picking_type
PurchaseRequisition --> stock_picking_type : many2one
class "stock.move" as stock_move
PurchaseRequisitionLine --> stock_move : many2one
class "purchase.requisition.line" as purchase_requisition_line
StockMove --|> purchase_requisition_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
