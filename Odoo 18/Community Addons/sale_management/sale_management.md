<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sales

- Version: v18
- Category: community
- Source: odoo/addons/sale_management
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

From quotations to invoices

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 10

## Detected Models

- `Digest`
- `ResCompany`
- `SaleOrder`
- `SaleOrderLine`
- `sale.order.option`
- `sale.order.template`
- `sale.order.template.line`
- `sale.order.template.option`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales - Models and Relations
class Digest
class ResCompany
class SaleOrder
class SaleOrderLine
class "sale.order.option" as sale_order_option
class "sale.order.template" as sale_order_template
class "sale.order.template.line" as sale_order_template_line
class "sale.order.template.option" as sale_order_template_option
ResCompany --> sale_order_template : many2one
SaleOrder --> sale_order_template : many2one
SaleOrder --|> sale_order_option : one2many
SaleOrderLine --|> sale_order_option : one2many
class "sale.order" as sale_order
sale_order_option --> sale_order : many2one
class "product.product" as product_product
sale_order_option --> product_product : many2one
class "sale.order.line" as sale_order_line
sale_order_option --> sale_order_line : many2one
class "uom.uom" as uom_uom
sale_order_option --> uom_uom : many2one
class "res.company" as res_company
sale_order_template --> res_company : many2one
class "mail.template" as mail_template
sale_order_template --> mail_template : many2one
sale_order_template --|> sale_order_template_line : one2many
sale_order_template --|> sale_order_template_option : one2many
class "account.journal" as account_journal
sale_order_template --> account_journal : many2one
sale_order_template_line --> sale_order_template : many2one
sale_order_template_line --> product_product : many2one
sale_order_template_line --> uom_uom : many2one
sale_order_template_option --> sale_order_template : many2one
sale_order_template_option --> product_product : many2one
sale_order_template_option --> uom_uom : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
