<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/sale_management
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/digest/digest|digest]]

## Summary

From quotations to invoices

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `DigestDigest`
- `ResCompany`
- `SaleOrder`
- `SaleOrderLine`
- `sale.order.template`
- `sale.order.template.line`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales - Models and Relations
class DigestDigest
class ResCompany
class SaleOrder
class SaleOrderLine
class "sale.order.template" as sale_order_template
class "sale.order.template.line" as sale_order_template_line
ResCompany --> sale_order_template : many2one
SaleOrder --> sale_order_template : many2one
class "res.company" as res_company
sale_order_template --> res_company : many2one
class "mail.template" as mail_template
sale_order_template --> mail_template : many2one
sale_order_template --|> sale_order_template_line : one2many
class "account.journal" as account_journal
sale_order_template --> account_journal : many2one
sale_order_template_line --> sale_order_template : many2one
class "product.product" as product_product
sale_order_template_line --> product_product : many2one
class "uom.uom" as uom_uom
sale_order_template_line .. uom_uom : many2many
sale_order_template_line --> uom_uom : many2one
sale_order_template_line --> sale_order_template_line : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


