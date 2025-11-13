<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Purchase Stock

- Version: v18
- Category: community
- Source: odoo/addons/purchase_stock
- Dependencies: [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 18/Community Addons/purchase/purchase|purchase]]

## Summary

Purchase Orders, Receipts, Vendor Bills for Stock

## XML Artifacts (detected)

- Views: 22
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 14

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductCategory`
- `product.template`
- `product.product`
- `SupplierInfo`
- `PurchaseOrder`
- `PurchaseOrderLine`
- `ResCompany`
- `ResPartner`
- `StockPicking`
- `StockWarehouse`
- `Orderpoint`
- `StockLot`
- `ProcurementGroup`
- `StockMove`
- `StockRule`
- `StockValuationLayer`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase Stock - Models and Relations
class AccountMove
class AccountMoveLine
class ProductCategory
class "product.template" as product_template
class "product.product" as product_product
class SupplierInfo
class PurchaseOrder
class PurchaseOrderLine
class ResCompany
class ResPartner
class StockPicking
class StockWarehouse
class Orderpoint
class StockLot
class ProcurementGroup
class StockMove
class StockRule
class StockValuationLayer
class "account.account" as account_account
ProductCategory --> account_account : many2one
product_template --> account_account : many2one
class "purchase.order.line" as purchase_order_line
product_product --|> purchase_order_line : one2many
class "stock.picking" as stock_picking
PurchaseOrder .. stock_picking : many2many
class "res.partner" as res_partner
PurchaseOrder --> res_partner : many2one
class "stock.picking.type" as stock_picking_type
PurchaseOrder --> stock_picking_type : many2one
class "procurement.group" as procurement_group
PurchaseOrder --> procurement_group : many2one
class "stock.move" as stock_move
PurchaseOrderLine --|> stock_move : one2many
class "stock.warehouse.orderpoint" as stock_warehouse_orderpoint
PurchaseOrderLine --> stock_warehouse_orderpoint : many2one
PurchaseOrderLine .. stock_move : many2many
class "stock.location" as stock_location
PurchaseOrderLine --> stock_location : many2one
PurchaseOrderLine --> procurement_group : many2one
ResPartner --|> purchase_order_line : one2many
class "purchase.order" as purchase_order
StockPicking --> purchase_order : many2one
class "stock.rule" as stock_rule
StockWarehouse --> stock_rule : many2one
class "product.supplierinfo" as product_supplierinfo
Orderpoint --> product_supplierinfo : many2one
Orderpoint --> res_partner : many2one
StockLot .. purchase_order : many2many
ProcurementGroup --|> purchase_order_line : one2many
StockMove --> purchase_order_line : many2one
StockMove .. purchase_order_line : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
