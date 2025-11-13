<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# MRP Subcontracting

- Version: v18
- Category: community
- Source: odoo/addons/mrp_subcontracting
- Dependencies: [[Odoo 18/Community Addons/mrp/mrp|mrp]]

## Summary

Subcontract Productions

## XML Artifacts (detected)

- Views: 21
- Actions: 1
- Menus: 0
- Rules (ir.rule): 14
- Access CSV entries: 16

## Detected Models

- `MrpBom`
- `MrpProduction`
- `SupplierInfo`
- `ProductProduct`
- `ResCompany`
- `ResPartner`
- `StockLocation`
- `StockMove`
- `StockMoveLine`
- `stock.picking`
- `StockQuant`
- `StockRule`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MRP Subcontracting - Models and Relations
class MrpBom
class MrpProduction
class SupplierInfo
class ProductProduct
class ResCompany
class ResPartner
class StockLocation
class StockMove
class StockMoveLine
class "stock.picking" as stock_picking
class StockQuant
class StockRule
class StockWarehouse
class "res.partner" as res_partner
MrpBom .. res_partner : many2many
class "stock.move.line" as stock_move_line
MrpProduction --|> stock_move_line : one2many
MrpProduction --> res_partner : many2one
class "product.product" as product_product
MrpProduction .. product_product : many2many
class "stock.location" as stock_location
ResCompany --> stock_location : many2one
ResPartner --> stock_location : many2one
class "mrp.bom" as mrp_bom
ResPartner .. mrp_bom : many2many
class "mrp.production" as mrp_production
ResPartner .. mrp_production : many2many
ResPartner .. stock_picking : many2many
StockLocation --|> res_partner : one2many
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
StockWarehouse --> stock_rule : many2one
class "stock.route" as stock_route
StockWarehouse --> stock_route : many2one
class "stock.picking.type" as stock_picking_type
StockWarehouse --> stock_picking_type : many2one
StockWarehouse --> stock_picking_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
