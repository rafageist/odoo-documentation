<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# MRP Subcontracting

- Scope: Community Addons
- Source: odoo/addons/mrp_subcontracting
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]]

## Summary

Subcontract Productions

## XML Artifacts (detected)

- Views: 20
- Actions: 1
- Menus: 0
- Rules (ir.rule): 13
- Access CSV entries: 16

## Detected Models

- `MrpBom`
- `MrpProduction`
- `ProductSupplierinfo`
- `ProductProduct`
- `ResCompany`
- `ResPartner`
- `StockLocation`
- `StockMove`
- `StockMoveLine`
- `StockPicking`
- `StockQuant`
- `StockRule`
- `StockWarehouse`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title MRP Subcontracting - Models and Relations
class MrpBom
class MrpProduction
class ProductSupplierinfo
class ProductProduct
class ResCompany
class ResPartner
class StockLocation
class StockMove
class StockMoveLine
class StockPicking
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
class "stock.picking" as stock_picking
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





