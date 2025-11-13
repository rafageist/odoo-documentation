<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Inventory

- Version: v19
- Category: community
- Source: odoo19/addons/stock
- Dependencies: [[Odoo 19/Community Addons/product/product|product]], [[Odoo 19/Community Addons/barcodes_gs1_nomenclature/barcodes_gs1_nomenclature|barcodes_gs1_nomenclature]], [[Odoo 19/Community Addons/digest/digest|digest]]

## Summary

Manage your stock and logistics activities

## XML Artifacts (detected)

- Views: 129
- Actions: 103
- Menus: 42
- Rules (ir.rule): 16
- Access CSV entries: 77

## Detected Models

- `BarcodeRule`
- `IrActionsReport`
- `ProductProduct`
- `ProductTemplate`
- `ProductCategory`
- `UomUom`
- `product.removal`
- `stock.putaway.rule`
- `ResCompany`
- `ResPartner`
- `ResUsers`
- `stock.location`
- `stock.route`
- `stock.lot`
- `stock.move`
- `stock.move.line`
- `stock.warehouse.orderpoint`
- `stock.package`
- `stock.package.history`
- `stock.package.type`
- `stock.picking.type`
- `stock.picking`
- `stock.quant`
- `stock.reference`
- `stock.rule`
- `stock.scrap`
- `stock.scrap.reason.tag`
- `stock.storage.category`
- `stock.storage.category.capacity`
- `stock.warehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inventory - Models and Relations
class BarcodeRule
class IrActionsReport
class ProductProduct
class ProductTemplate
class ProductCategory
class UomUom
class "product.removal" as product_removal
class "stock.putaway.rule" as stock_putaway_rule
class ResCompany
class ResPartner
class ResUsers
class "stock.location" as stock_location
class "stock.route" as stock_route
class "stock.lot" as stock_lot
class "stock.move" as stock_move
class "stock.move.line" as stock_move_line
class "stock.warehouse.orderpoint" as stock_warehouse_orderpoint
class "stock.package" as stock_package
class "stock.package.history" as stock_package_history
class "stock.package.type" as stock_package_type
class "stock.picking.type" as stock_picking_type
class "stock.picking" as stock_picking
class "stock.quant" as stock_quant
class "stock.reference" as stock_reference
class "stock.rule" as stock_rule
class "stock.scrap" as stock_scrap
class "stock.scrap.reason.tag" as stock_scrap_reason_tag
class "stock.storage.category" as stock_storage_category
class "stock.storage.category.capacity" as stock_storage_category_capacity
class "stock.warehouse" as stock_warehouse
ProductProduct --|> stock_quant : one2many
ProductProduct --|> stock_move : one2many
ProductProduct --|> stock_warehouse_orderpoint : one2many
ProductProduct --|> stock_putaway_rule : one2many
ProductProduct --|> stock_storage_category_capacity : one2many
class "res.users" as res_users
ProductTemplate --> res_users : many2one
ProductTemplate --> stock_location : many2one
ProductTemplate --> stock_location : many2one
class "ir.sequence" as ir_sequence
ProductTemplate --> ir_sequence : many2one
ProductTemplate --> stock_location : many2one
ProductTemplate --> stock_warehouse : many2one
ProductTemplate .. stock_route : many2many
ProductCategory .. stock_route : many2many
ProductCategory --> product_removal : many2one
ProductCategory .. stock_route : many2many
ProductCategory .. stock_route : many2many
ProductCategory --|> stock_putaway_rule : one2many
UomUom --> stock_package_type : many2one
class "product.product" as product_product
stock_putaway_rule --> product_product : many2one
class "product.category" as product_category
stock_putaway_rule --> product_category : many2one
stock_putaway_rule --> stock_location : many2one
stock_putaway_rule --> stock_location : many2one
class "res.company" as res_company
stock_putaway_rule --> res_company : many2one
stock_putaway_rule .. stock_package_type : many2many
stock_putaway_rule --> stock_storage_category : many2one
ResCompany --> stock_location : many2one
class "mail.template" as mail_template
ResCompany --> mail_template : many2one
ResPartner --> stock_location : many2one
ResPartner --> stock_location : many2one
stock_location --> stock_location : many2one
stock_location --|> stock_location : one2many
stock_location .. stock_location : many2many
stock_location --> res_company : many2one
stock_location --> product_removal : many2one
stock_location --|> stock_putaway_rule : one2many
stock_location --|> stock_quant : one2many
stock_location --|> stock_warehouse : one2many
stock_location --> stock_warehouse : many2one
stock_location --> stock_storage_category : many2one
stock_location --|> stock_move_line : one2many
stock_location --|> stock_move_line : one2many
stock_route --|> stock_rule : one2many
stock_route --> stock_warehouse : many2one
stock_route --> stock_warehouse : many2one
stock_route --> res_company : many2one
class "product.template" as product_template
stock_route .. product_template : many2many
stock_route .. product_category : many2many
stock_route --|> stock_warehouse : one2many
stock_route .. stock_warehouse : many2many
stock_lot --> product_product : many2one
class "uom.uom" as uom_uom
stock_lot --> uom_uom : many2one
stock_lot --|> stock_quant : one2many
stock_lot --> res_company : many2one
stock_lot .. stock_picking : many2many
class "res.partner" as res_partner
stock_lot .. res_partner : many2many
stock_lot --> stock_location : many2one
stock_move --> res_company : many2one
stock_move --> product_product : many2one
class "product.template.attribute.value" as product_template_attribute_value
stock_move .. product_template_attribute_value : many2many
stock_move .. uom_uom : many2many
stock_move --> uom_uom : many2one
stock_move --> product_template : many2one
stock_move --> stock_location : many2one
stock_move --> stock_location : many2one
stock_move --> stock_location : many2one
stock_move --> res_partner : many2one
stock_move .. stock_move : many2many
stock_move .. stock_move : many2many
stock_move --> stock_picking : many2one
stock_move --> stock_scrap : many2one
stock_move .. stock_reference : many2many
stock_move --> stock_rule : many2one
stock_move --> stock_picking_type : many2one
stock_move --|> stock_move_line : one2many
stock_move --|> stock_package : one2many
stock_move --> stock_move : many2one
stock_move --|> stock_move : one2many
stock_move --> res_partner : many2one
stock_move .. stock_route : many2many
stock_move --> stock_warehouse : many2one
stock_move --> stock_warehouse_orderpoint : many2one
stock_move .. stock_lot : many2many
stock_move --> uom_uom : many2one
stock_move_line --> stock_picking : many2one
stock_move_line --> stock_move : many2one
stock_move_line --> res_company : many2one
stock_move_line --> product_product : many2one
stock_move_line .. uom_uom : many2many
stock_move_line --> uom_uom : many2one
stock_move_line --> stock_package : many2one
stock_move_line --> stock_lot : many2one
stock_move_line --> stock_package : many2one
stock_move_line --> stock_package_history : many2one
stock_move_line --> res_partner : many2one
stock_move_line --> stock_location : many2one
stock_move_line --> stock_location : many2one
stock_move_line --> stock_picking_type : many2one
stock_move_line .. stock_move_line : many2many
stock_move_line .. stock_move_line : many2many
stock_move_line --> stock_quant : many2one
stock_warehouse_orderpoint --> stock_warehouse : many2one
stock_warehouse_orderpoint --> stock_location : many2one
stock_warehouse_orderpoint --> product_template : many2one
stock_warehouse_orderpoint --> product_product : many2one
stock_warehouse_orderpoint --> product_category : many2one
stock_warehouse_orderpoint --> uom_uom : many2one
stock_warehouse_orderpoint .. uom_uom : many2many
stock_warehouse_orderpoint --> uom_uom : many2one
stock_warehouse_orderpoint --> res_company : many2one
stock_warehouse_orderpoint --|> stock_location : one2many
stock_warehouse_orderpoint .. stock_rule : many2many
stock_warehouse_orderpoint --> stock_route : many2one
stock_warehouse_orderpoint --> stock_route : many2one
stock_package --|> stock_quant : one2many
stock_package --|> stock_quant : one2many
stock_package --> stock_package_type : many2one
stock_package --> stock_location : many2one
stock_package --> stock_location : many2one
stock_package --> res_company : many2one
stock_package --> res_partner : many2one
stock_package --> stock_package : many2one
stock_package --|> stock_package : one2many
stock_package --|> stock_package : one2many
stock_package --> stock_package : many2one
stock_package --> stock_package : many2one
stock_package --|> stock_package : one2many
stock_package --|> stock_move_line : one2many
stock_package .. stock_picking : many2many
stock_package_history --> res_company : many2one
stock_package_history --> stock_location : many2one
stock_package_history --> stock_location : many2one
stock_package_history --|> stock_move_line : one2many
stock_package_history --> stock_package : many2one
stock_package_history --> stock_package_type : many2one
stock_package_history --> stock_package : many2one
stock_package_history --> stock_package : many2one
stock_package_history --> stock_package : many2one
stock_package_history .. stock_picking : many2many
stock_package_type --> ir_sequence : many2one
stock_package_type --> res_company : many2one
stock_package_type --|> stock_storage_category_capacity : one2many
stock_package_type .. stock_route : many2many
stock_picking_type --> ir_sequence : many2one
stock_picking_type --> stock_location : many2one
stock_picking_type --> stock_location : many2one
stock_picking_type --> stock_picking_type : many2one
stock_picking_type --> stock_warehouse : many2one
stock_picking_type --> res_company : many2one
stock_picking_type .. res_users : many2many
stock_picking --> stock_picking : many2one
stock_picking --|> stock_picking : one2many
stock_picking --> stock_picking : many2one
stock_picking --|> stock_picking : one2many
stock_picking .. stock_reference : many2many
stock_picking --> stock_location : many2one
stock_picking --> stock_location : many2one
stock_picking --|> stock_move : one2many
stock_picking --> stock_picking_type : many2one
stock_picking --> res_partner : many2one
stock_picking --> res_partner : many2one
stock_picking --> res_company : many2one
stock_picking --> res_users : many2one
stock_picking --|> stock_move_line : one2many
stock_picking .. stock_package_history : many2many
stock_picking --> res_partner : many2one
stock_picking --> product_product : many2one
stock_picking --> stock_lot : many2one
class "res.country" as res_country
stock_picking --> res_country : many2one
stock_quant --> product_product : many2one
stock_quant --> product_template : many2one
stock_quant --> uom_uom : many2one
stock_quant --> stock_location : many2one
stock_quant --> stock_warehouse : many2one
stock_quant --> stock_lot : many2one
stock_quant --> stock_package : many2one
stock_quant --> res_partner : many2one
stock_quant --> res_users : many2one
stock_reference .. stock_move : many2many
stock_reference .. stock_picking : many2many
stock_rule --> res_company : many2one
stock_rule --> stock_location : many2one
stock_rule --> stock_location : many2one
stock_rule --> stock_route : many2one
stock_rule --> stock_picking_type : many2one
stock_rule --> res_partner : many2one
stock_rule --> stock_warehouse : many2one
stock_scrap --> res_company : many2one
stock_scrap --> product_product : many2one
stock_scrap .. uom_uom : many2many
stock_scrap --> uom_uom : many2one
stock_scrap --> stock_lot : many2one
stock_scrap --> stock_package : many2one
stock_scrap --> res_partner : many2one
stock_scrap --|> stock_move : one2many
stock_scrap --> stock_picking : many2one
stock_scrap --> stock_location : many2one
stock_scrap --> stock_location : many2one
stock_scrap .. stock_scrap_reason_tag : many2many
stock_storage_category --|> stock_storage_category_capacity : one2many
stock_storage_category --|> stock_storage_category_capacity : one2many
stock_storage_category --|> stock_storage_category_capacity : one2many
stock_storage_category --|> stock_location : one2many
stock_storage_category --> res_company : many2one
stock_storage_category_capacity --> stock_storage_category : many2one
stock_storage_category_capacity --> product_product : many2one
stock_storage_category_capacity --> stock_package_type : many2one
stock_storage_category_capacity --> res_company : many2one
stock_warehouse --> res_company : many2one
stock_warehouse --> res_partner : many2one
stock_warehouse --> stock_location : many2one
stock_warehouse --> stock_location : many2one
stock_warehouse .. stock_route : many2many
stock_warehouse --> stock_location : many2one
stock_warehouse --> stock_location : many2one
stock_warehouse --> stock_location : many2one
stock_warehouse --> stock_location : many2one
stock_warehouse --> stock_rule : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_picking_type : many2one
stock_warehouse --> stock_route : many2one
stock_warehouse --> stock_route : many2one
stock_warehouse .. stock_warehouse : many2many
stock_warehouse --|> stock_route : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
