<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Purchase Stock

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/purchase_stock
- Dependencies: [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 19/Community Addons/purchase/purchase|purchase]]

## Summary

Purchase Orders, Receipts, Vendor Bills for Stock

## XML Artifacts (detected)

- Views: 21
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 14

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductTemplate`
- `ProductProduct`
- `ProductSupplierinfo`
- `PurchaseOrder`
- `PurchaseOrderLine`
- `ResCompany`
- `ResPartner`
- `StockPicking`
- `StockWarehouse`
- `StockWarehouseOrderpoint`
- `StockLot`
- `StockMove`
- `StockReference`
- `StockRule`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase Stock - Models and Relations
class AccountMove
class AccountMoveLine
class ProductTemplate
class ProductProduct
class ProductSupplierinfo
class PurchaseOrder
class PurchaseOrderLine
class ResCompany
class ResPartner
class StockPicking
class StockWarehouse
class StockWarehouseOrderpoint
class StockLot
class StockMove
class StockReference
class StockRule
class "purchase.order.line" as purchase_order_line
ProductProduct --|> purchase_order_line : one2many
class "stock.picking" as stock_picking
PurchaseOrder .. stock_picking : many2many
class "res.partner" as res_partner
PurchaseOrder --> res_partner : many2one
class "stock.picking.type" as stock_picking_type
PurchaseOrder --> stock_picking_type : many2one
class "stock.reference" as stock_reference
PurchaseOrder .. stock_reference : many2many
class "stock.move" as stock_move
PurchaseOrderLine --|> stock_move : one2many
class "stock.warehouse.orderpoint" as stock_warehouse_orderpoint
PurchaseOrderLine --> stock_warehouse_orderpoint : many2one
PurchaseOrderLine .. stock_move : many2many
class "stock.location" as stock_location
PurchaseOrderLine --> stock_location : many2one
ResPartner --|> purchase_order_line : one2many
class "purchase.order" as purchase_order
StockPicking --> purchase_order : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
class "product.supplierinfo" as product_supplierinfo
StockWarehouseOrderpoint --> product_supplierinfo : many2one
StockWarehouseOrderpoint --> res_partner : many2one
StockWarehouseOrderpoint --> res_partner : many2one
StockLot .. purchase_order : many2many
StockMove --> purchase_order_line : many2one
StockMove .. purchase_order_line : many2many
StockReference .. purchase_order : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


