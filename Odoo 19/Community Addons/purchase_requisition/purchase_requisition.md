<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Purchase Agreements

- Version: v19
- Category: community
- Source: odoo19/addons/purchase_requisition
- Dependencies: [[Odoo 19/Community Addons/purchase/purchase|purchase]]
## XML Artifacts (detected)

- Views: 12
- Actions: 4
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 7

## Detected Models

- `ProductSupplierinfo`
- `ProductProduct`
- `purchase.order.group`
- `PurchaseOrder`
- `PurchaseOrderLine`
- `purchase.requisition`
- `purchase.requisition.line`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase Agreements - Models and Relations
class ProductSupplierinfo
class ProductProduct
class "purchase.order.group" as purchase_order_group
class PurchaseOrder
class PurchaseOrderLine
class "purchase.requisition" as purchase_requisition
class "purchase.requisition.line" as purchase_requisition_line
ProductSupplierinfo --> purchase_requisition : many2one
ProductSupplierinfo --> purchase_requisition_line : many2one
class "purchase.order" as purchase_order
purchase_order_group --|> purchase_order : one2many
PurchaseOrder --> purchase_requisition : many2one
PurchaseOrder --> purchase_order_group : many2one
PurchaseOrder --|> purchase_order : one2many
class "res.partner" as res_partner
purchase_requisition --> res_partner : many2one
class "res.users" as res_users
purchase_requisition --> res_users : many2one
class "res.company" as res_company
purchase_requisition --> res_company : many2one
purchase_requisition --|> purchase_order : one2many
purchase_requisition --|> purchase_requisition_line : one2many
class "product.product" as product_product
purchase_requisition --> product_product : many2one
class "res.currency" as res_currency
purchase_requisition --> res_currency : many2one
purchase_requisition_line --> product_product : many2one
class "uom.uom" as uom_uom
purchase_requisition_line --> uom_uom : many2one
purchase_requisition_line --> purchase_requisition : many2one
purchase_requisition_line --> res_company : many2one
class "product.supplierinfo" as product_supplierinfo
purchase_requisition_line --|> product_supplierinfo : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
