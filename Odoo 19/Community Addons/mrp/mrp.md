<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Manufacturing

- Version: v19
- Category: community
- Source: odoo19/addons/mrp
- Dependencies: [[Odoo 19/Community Addons/product/product|product]], [[Odoo 19/Community Addons/stock/stock|stock]], [[Odoo 19/Community Addons/resource/resource|resource]]

## Summary

Manufacturing Orders & BOMs

## XML Artifacts (detected)

- Views: 85
- Actions: 61
- Menus: 21
- Rules (ir.rule): 9
- Access CSV entries: 54

## Detected Models

- `IrAttachment`
- `mrp.bom`
- `mrp.bom.line`
- `mrp.bom.byproduct`
- `mrp.production.group`
- `mrp.production`
- `mrp.routing.workcenter`
- `mrp.unbuild`
- `mrp.workcenter`
- `mrp.workcenter.tag`
- `mrp.workcenter.productivity.loss.type`
- `mrp.workcenter.productivity.loss`
- `mrp.workcenter.productivity`
- `mrp.workcenter.capacity`
- `mrp.workorder`
- `ProductTemplate`
- `ProductProduct`
- `ProductDocument`
- `ResCompany`
- `StockLot`
- `StockMove`
- `StockMoveLine`
- `StockWarehouseOrderpoint`
- `StockPickingType`
- `StockPicking`
- `StockQuant`
- `StockReference`
- `StockRule`
- `StockScrap`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Manufacturing - Models and Relations
class IrAttachment
class "mrp.bom" as mrp_bom
class "mrp.bom.line" as mrp_bom_line
class "mrp.bom.byproduct" as mrp_bom_byproduct
class "mrp.production.group" as mrp_production_group
class "mrp.production" as mrp_production
class "mrp.routing.workcenter" as mrp_routing_workcenter
class "mrp.unbuild" as mrp_unbuild
class "mrp.workcenter" as mrp_workcenter
class "mrp.workcenter.tag" as mrp_workcenter_tag
class "mrp.workcenter.productivity.loss.type" as mrp_workcenter_productivity_loss_type
class "mrp.workcenter.productivity.loss" as mrp_workcenter_productivity_loss
class "mrp.workcenter.productivity" as mrp_workcenter_productivity
class "mrp.workcenter.capacity" as mrp_workcenter_capacity
class "mrp.workorder" as mrp_workorder
class ProductTemplate
class ProductProduct
class ProductDocument
class ResCompany
class StockLot
class StockMove
class StockMoveLine
class StockWarehouseOrderpoint
class StockPickingType
class StockPicking
class StockQuant
class StockReference
class StockRule
class StockScrap
class StockWarehouse
class "product.template" as product_template
mrp_bom --> product_template : many2one
class "product.product" as product_product
mrp_bom --> product_product : many2one
mrp_bom --|> mrp_bom_line : one2many
mrp_bom --|> mrp_bom_byproduct : one2many
class "uom.uom" as uom_uom
mrp_bom --> uom_uom : many2one
mrp_bom --|> mrp_routing_workcenter : one2many
class "stock.picking.type" as stock_picking_type
mrp_bom --> stock_picking_type : many2one
class "res.company" as res_company
mrp_bom --> res_company : many2one
class "product.template.attribute.value" as product_template_attribute_value
mrp_bom .. product_template_attribute_value : many2many
mrp_bom_line --> product_product : many2one
mrp_bom_line --> product_template : many2one
mrp_bom_line --> uom_uom : many2one
mrp_bom_line --> mrp_bom : many2one
mrp_bom_line --> product_template : many2one
mrp_bom_line .. product_template_attribute_value : many2many
mrp_bom_line --|> mrp_routing_workcenter : one2many
mrp_bom_line --> mrp_routing_workcenter : many2one
mrp_bom_line --> mrp_bom : many2one
mrp_bom_line --|> mrp_bom_line : one2many
mrp_bom_byproduct --> product_product : many2one
mrp_bom_byproduct --> uom_uom : many2one
mrp_bom_byproduct --> mrp_bom : many2one
mrp_bom_byproduct --|> mrp_routing_workcenter : one2many
mrp_bom_byproduct --> mrp_routing_workcenter : many2one
mrp_bom_byproduct .. product_template_attribute_value : many2many
mrp_production_group --|> mrp_production : one2many
mrp_production_group .. mrp_production_group : many2many
mrp_production_group .. mrp_production_group : many2many
mrp_production --> product_product : many2one
mrp_production --> mrp_production_group : many2one
mrp_production .. product_template_attribute_value : many2many
mrp_production .. product_template_attribute_value : many2many
mrp_production --> mrp_workcenter : many2one
mrp_production --> product_template : many2one
mrp_production .. uom_uom : many2many
mrp_production --> uom_uom : many2one
class "stock.lot" as stock_lot
mrp_production .. stock_lot : many2many
mrp_production --> stock_picking_type : many2one
class "stock.location" as stock_location
mrp_production --> stock_location : many2one
mrp_production --> stock_location : many2one
mrp_production --> stock_location : many2one
mrp_production --> mrp_bom : many2one
class "stock.move" as stock_move
mrp_production --|> stock_move : one2many
mrp_production --|> stock_move : one2many
mrp_production --|> stock_move : one2many
mrp_production --|> stock_move : one2many
mrp_production --|> stock_move : one2many
class "stock.move.line" as stock_move_line
mrp_production --|> stock_move_line : one2many
mrp_production --|> mrp_workorder : one2many
mrp_production --|> stock_move : one2many
class "res.users" as res_users
mrp_production --> res_users : many2one
mrp_production --> res_company : many2one
class "stock.reference" as stock_reference
mrp_production .. stock_reference : many2many
class "stock.warehouse.orderpoint" as stock_warehouse_orderpoint
mrp_production --> stock_warehouse_orderpoint : many2one
class "stock.scrap" as stock_scrap
mrp_production --|> stock_scrap : one2many
mrp_production --|> mrp_unbuild : one2many
mrp_production --> stock_location : many2one
class "stock.picking" as stock_picking
mrp_production .. stock_picking : many2many
mrp_routing_workcenter --> mrp_workcenter : many2one
mrp_routing_workcenter --> mrp_bom : many2one
mrp_routing_workcenter --> res_company : many2one
mrp_routing_workcenter --|> mrp_workorder : one2many
mrp_routing_workcenter .. product_template_attribute_value : many2many
mrp_routing_workcenter .. mrp_routing_workcenter : many2many
mrp_routing_workcenter .. mrp_routing_workcenter : many2many
mrp_unbuild --> product_product : many2one
mrp_unbuild --> res_company : many2one
mrp_unbuild --> uom_uom : many2one
mrp_unbuild --> mrp_bom : many2one
mrp_unbuild --> mrp_production : many2one
mrp_unbuild --> mrp_bom : many2one
mrp_unbuild .. stock_lot : many2many
mrp_unbuild --> stock_lot : many2one
mrp_unbuild --> stock_location : many2one
mrp_unbuild --> stock_location : many2one
mrp_unbuild --|> stock_move : one2many
mrp_unbuild --|> stock_move : one2many
class "res.currency" as res_currency
mrp_workcenter --> res_currency : many2one
mrp_workcenter --|> mrp_routing_workcenter : one2many
mrp_workcenter --|> mrp_workorder : one2many
mrp_workcenter --|> mrp_workcenter_productivity : one2many
mrp_workcenter .. mrp_workcenter : many2many
mrp_workcenter .. mrp_workcenter_tag : many2many
mrp_workcenter --|> mrp_workcenter_capacity : one2many
mrp_workcenter_productivity_loss --> mrp_workcenter_productivity_loss_type : many2one
mrp_workcenter_productivity --> mrp_production : many2one
mrp_workcenter_productivity --> mrp_workcenter : many2one
mrp_workcenter_productivity --> res_company : many2one
mrp_workcenter_productivity --> mrp_workorder : many2one
mrp_workcenter_productivity --> res_users : many2one
mrp_workcenter_productivity --> mrp_workcenter_productivity_loss : many2one
mrp_workcenter_capacity --> mrp_workcenter : many2one
mrp_workcenter_capacity --> product_product : many2one
mrp_workcenter_capacity --> uom_uom : many2one
mrp_workorder --> mrp_workcenter : many2one
mrp_workorder .. product_template_attribute_value : many2many
mrp_workorder --> mrp_production : many2one
mrp_workorder --> mrp_bom : many2one
class "resource.calendar.leaves" as resource_calendar_leaves
mrp_workorder --> resource_calendar_leaves : many2one
mrp_workorder --> mrp_routing_workcenter : many2one
mrp_workorder --|> stock_move : one2many
mrp_workorder --|> stock_move : one2many
mrp_workorder --|> stock_move_line : one2many
mrp_workorder .. stock_lot : many2many
mrp_workorder --|> mrp_workcenter_productivity : one2many
mrp_workorder --|> res_users : one2many
mrp_workorder --> res_users : many2one
mrp_workorder --|> stock_scrap : one2many
mrp_workorder .. mrp_workorder : many2many
mrp_workorder .. mrp_workorder : many2many
ProductTemplate --|> mrp_bom_line : one2many
ProductTemplate --|> mrp_bom : one2many
ProductProduct --|> mrp_bom : one2many
ProductProduct --|> mrp_bom_line : one2many
StockMove --> mrp_production : many2one
StockMove --> mrp_production : many2one
StockMove --> mrp_production : many2one
StockMove --> mrp_production_group : many2one
StockMove --> mrp_unbuild : many2one
StockMove --> mrp_unbuild : many2one
StockMove --|> mrp_routing_workcenter : one2many
StockMove --> mrp_routing_workcenter : many2one
StockMove --> mrp_workorder : many2one
StockMove --> mrp_bom_line : many2one
StockMove --> mrp_bom_byproduct : many2one
StockMove .. stock_lot : many2many
StockMoveLine --> mrp_workorder : many2one
StockMoveLine --> mrp_production : many2one
StockWarehouseOrderpoint --> mrp_bom : many2one
StockWarehouseOrderpoint --> mrp_bom : many2one
StockPicking --|> mrp_production : one2many
StockPicking --> mrp_production_group : many2one
StockReference .. mrp_production : many2many
StockScrap --> mrp_production : many2one
StockScrap --> mrp_workorder : many2one
StockScrap --> mrp_bom : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
StockWarehouse --> stock_rule : many2one
StockWarehouse --> stock_rule : many2one
StockWarehouse --> stock_rule : many2one
StockWarehouse --> stock_picking_type : many2one
StockWarehouse --> stock_picking_type : many2one
StockWarehouse --> stock_picking_type : many2one
class "stock.route" as stock_route
StockWarehouse --> stock_route : many2one
StockWarehouse --> stock_location : many2one
StockWarehouse --> stock_location : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
