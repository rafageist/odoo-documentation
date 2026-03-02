<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Dropship and Subcontracting Management

- Scope: Community Addons
- Source: odoo/addons/mrp_subcontracting_dropshipping
- Dependencies: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]], [[docs/Community Addons/stock_dropshipping/stock_dropshipping|stock_dropshipping]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `ResCompany`
- `StockMove`
- `StockWarehouseOrderpoint`
- `StockPicking`
- `StockRule`
- `StockWarehouse`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Dropship and Subcontracting Management - Models and Relations
class PurchaseOrder
class ResCompany
class StockMove
class StockWarehouseOrderpoint
class StockPicking
class StockRule
class StockWarehouse
class "stock.picking.type" as stock_picking_type
ResCompany --> stock_picking_type : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





