<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# eCommerce

- Version: v18
- Category: community
- Source: odoo/addons/website_sale
- Dependencies: [[Odoo 18/Community Addons/website/website|website]], [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/website_payment/website_payment|website_payment]], [[Odoo 18/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 18/Community Addons/portal_rating/portal_rating|portal_rating]], [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/delivery/delivery|delivery]]

## Summary

Sell your products online

## XML Artifacts (detected)

- Views: 56
- Actions: 25
- Menus: 23
- Rules (ir.rule): 5
- Access CSV entries: 58

## Detected Models

- `AccountMove`
- `CrmTeam`
- `delivery.carrier`
- `Digest`
- `PaymentToken`
- `ProductAttribute`
- `ProductDocument`
- `product.image`
- `ProductPricelist`
- `ProductPricelistItem`
- `Product`
- `product.public.category`
- `product.ribbon`
- `product.tag`
- `product.template`
- `ProductTemplateAttributeLine`
- `ProductTemplateAttributeValue`
- `ResCompany`
- `ResPartner`
- `SaleOrder`
- `SaleOrderLine`
- `Website`
- `website.base.unit`
- `Menu`
- `website.sale.extra.field`
- `WebsiteSnippetFilter`
- `WebsiteTrack`
- `WebsiteVisitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title eCommerce - Models and Relations
class AccountMove
class CrmTeam
class "delivery.carrier" as delivery_carrier
class Digest
class PaymentToken
class ProductAttribute
class ProductDocument
class "product.image" as product_image
class ProductPricelist
class ProductPricelistItem
class Product
class "product.public.category" as product_public_category
class "product.ribbon" as product_ribbon
class "product.tag" as product_tag
class "product.template" as product_template
class ProductTemplateAttributeLine
class ProductTemplateAttributeValue
class ResCompany
class ResPartner
class SaleOrder
class SaleOrderLine
class Website
class "website.base.unit" as website_base_unit
class Menu
class "website.sale.extra.field" as website_sale_extra_field
class WebsiteSnippetFilter
class WebsiteTrack
class WebsiteVisitor
class website
AccountMove --> website : many2one
CrmTeam --|> website : one2many
product_image --> product_template : many2one
class "product.product" as product_product
product_image --> product_product : many2one
ProductPricelist --> website : many2one
Product --> product_ribbon : many2one
Product --|> product_image : one2many
Product --> website_base_unit : many2one
product_public_category --> product_public_category : many2one
product_public_category --|> product_public_category : one2many
product_public_category .. product_public_category : many2many
product_public_category .. product_template : many2many
product_template .. product_template : many2many
product_template .. product_product : many2many
product_template --> product_ribbon : many2one
product_template .. product_public_category : many2many
product_template --|> product_image : one2many
product_template --> website_base_unit : many2one
class "sale.order" as sale_order
ResPartner --> sale_order : many2one
SaleOrder --> website : many2one
class "sale.order.line" as sale_order_line
SaleOrder --|> sale_order_line : one2many
class "res.users" as res_users
Website --> res_users : many2one
class "crm.team" as crm_team
Website --> crm_team : many2one
class "mail.template" as mail_template
Website --> mail_template : many2one
Website --|> website_sale_extra_field : one2many
class "account.fiscal.position" as account_fiscal_position
Website --> account_fiscal_position : many2one
class "product.pricelist" as product_pricelist
Website --> product_pricelist : many2one
class "res.currency" as res_currency
Website --> res_currency : many2one
Website --|> product_pricelist : one2many
Website --|> product_pricelist : one2many
website_sale_extra_field --> website : many2one
class "ir.model.fields" as ir_model_fields
website_sale_extra_field --> ir_model_fields : many2one
WebsiteTrack --> product_product : many2one
WebsiteVisitor .. product_product : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
