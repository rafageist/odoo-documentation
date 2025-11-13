<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Purchase

- Version: v18
- Category: community
- Source: odoo/addons/purchase
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]

## Summary

Purchase orders, tenders and agreements

## XML Artifacts (detected)

- Views: 44
- Actions: 18
- Menus: 20
- Rules (ir.rule): 8
- Access CSV entries: 42

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `AccountAnalyticAccount`
- `AccountAnalyticApplicability`
- `IrActionsReport`
- `product.template`
- `product.product`
- `ProductSupplierinfo`
- `ProductPackaging`
- `purchase.bill.line.match`
- `purchase.order`
- `purchase.order.line`
- `Company`
- `res.partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Purchase - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class AccountAnalyticAccount
class AccountAnalyticApplicability
class IrActionsReport
class "product.template" as product_template
class "product.product" as product_product
class ProductSupplierinfo
class ProductPackaging
class "purchase.bill.line.match" as purchase_bill_line_match
class "purchase.order" as purchase_order
class "purchase.order.line" as purchase_order_line
class Company
class "res.partner" as res_partner
class "purchase.bill.union" as purchase_bill_union
AccountMove --> purchase_bill_union : many2one
AccountMove --> purchase_order : many2one
AccountMoveLine --> purchase_order_line : many2one
AccountMoveLine --> purchase_order : many2one
purchase_bill_line_match --> purchase_order_line : many2one
class "account.move.line" as account_move_line
purchase_bill_line_match --> account_move_line : many2one
class "res.company" as res_company
purchase_bill_line_match --> res_company : many2one
purchase_bill_line_match --> res_partner : many2one
purchase_bill_line_match --> product_product : many2one
class "uom.uom" as uom_uom
purchase_bill_line_match --> uom_uom : many2one
purchase_bill_line_match --> purchase_order : many2one
class "account.move" as account_move
purchase_bill_line_match --> account_move : many2one
class "res.currency" as res_currency
purchase_bill_line_match --> res_currency : many2one
purchase_bill_line_match --> uom_uom : many2one
purchase_order --> res_partner : many2one
purchase_order --> res_partner : many2one
purchase_order --> res_currency : many2one
purchase_order --|> purchase_order_line : one2many
purchase_order .. account_move : many2many
class "account.fiscal.position" as account_fiscal_position
purchase_order --> account_fiscal_position : many2one
class "res.country" as res_country
purchase_order --> res_country : many2one
class "account.payment.term" as account_payment_term
purchase_order --> account_payment_term : many2one
class "account.incoterms" as account_incoterms
purchase_order --> account_incoterms : many2one
purchase_order --> product_product : many2one
class "res.users" as res_users
purchase_order --> res_users : many2one
purchase_order --> res_company : many2one
class "account.tax" as account_tax
purchase_order_line .. account_tax : many2many
purchase_order_line --> uom_uom : many2one
purchase_order_line --> product_product : many2one
purchase_order_line --> purchase_order : many2one
purchase_order_line --> res_company : many2one
purchase_order_line --|> account_move_line : one2many
purchase_order_line --> res_partner : many2one
class "product.packaging" as product_packaging
purchase_order_line --> product_packaging : many2one
class "product.template.attribute.value" as product_template_attribute_value
purchase_order_line .. product_template_attribute_value : many2many
res_partner --> res_currency : many2one
res_partner --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
