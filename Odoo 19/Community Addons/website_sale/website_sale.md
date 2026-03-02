<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# eCommerce

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_sale
- Dependencies: [[Odoo 19/Community Addons/website/website|website]], [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/website_payment/website_payment|website_payment]], [[Odoo 19/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 19/Community Addons/portal_rating/portal_rating|portal_rating]], [[Odoo 19/Community Addons/digest/digest|digest]], [[Odoo 19/Community Addons/delivery/delivery|delivery]], [[Odoo 19/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Sell your products online

## XML Artifacts (detected)

- Views: 56
- Actions: 28
- Menus: 24
- Rules (ir.rule): 6
- Access CSV entries: 67

## Detected Models

- `AccountMove`
- `CrmTeam`
- `delivery.carrier`
- `DigestDigest`
- `PaymentToken`
- `ProductAttribute`
- `ProductDocument`
- `product.feed`
- `product.image`
- `ProductPricelist`
- `ProductPricelistItem`
- `ProductProduct`
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
- `website.checkout.step`
- `WebsiteMenu`
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
class DigestDigest
class PaymentToken
class ProductAttribute
class ProductDocument
class "product.feed" as product_feed
class "product.image" as product_image
class ProductPricelist
class ProductPricelistItem
class ProductProduct
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
class "website.checkout.step" as website_checkout_step
class WebsiteMenu
class "website.sale.extra.field" as website_sale_extra_field
class WebsiteSnippetFilter
class WebsiteTrack
class WebsiteVisitor
class website
AccountMove --> website : many2one
CrmTeam --|> website : one2many
product_feed --> website : many2one
class "product.pricelist" as product_pricelist
product_feed --> product_pricelist : many2one
class "res.lang" as res_lang
product_feed --> res_lang : many2one
product_feed .. product_public_category : many2many
product_image --> product_template : many2one
class "product.product" as product_product
product_image --> product_product : many2one
ProductPricelist --> website : many2one
ProductProduct --> product_ribbon : many2one
ProductProduct --|> product_image : one2many
ProductProduct --> website_base_unit : many2one
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
class "res.currency" as res_currency
Website --> res_currency : many2one
Website --|> product_pricelist : one2many
Website --> mail_template : many2one
website_checkout_step --> website : many2one
website_sale_extra_field --> website : many2one
class "ir.model.fields" as ir_model_fields
website_sale_extra_field --> ir_model_fields : many2one
WebsiteTrack --> product_product : many2one
WebsiteVisitor .. product_product : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

