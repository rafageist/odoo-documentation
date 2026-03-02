<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Dropship and Subcontracting Management

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/mrp_subcontracting_dropshipping
- Dependencies: [[Odoo 19/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]], [[Odoo 19/Community Addons/stock_dropshipping/stock_dropshipping|stock_dropshipping]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


