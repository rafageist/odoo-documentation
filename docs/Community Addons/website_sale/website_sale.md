<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# eCommerce

- Scope: Community Addons
- Source: odoo/addons/website_sale
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/website_payment/website_payment|website_payment]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/portal_rating/portal_rating|portal_rating]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/delivery/delivery|delivery]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



## Curated analysis

### Functional role
- `website_sale` is the public commerce layer that turns products, prices, delivery methods, and payment-ready orders into a storefront experience.
- It is not just a website skin over `sale`; it adds website-specific pricing, checkout steps, product feeds, ribbons, visitor tracking, and cart/session behavior.

### Operational footprint
- The controller layer is broad: cart, checkout, delivery, payment, variant resolution, product configurator, reorder, and feeds each have their own entry point.
- The model layer extends both website and sales concepts, especially around `website.py`, `sale_order.py`, pricelists, and product presentation metadata.

### Evidence
- Source files: `odoo19/addons/website_sale/controllers/cart.py`, `odoo19/addons/website_sale/controllers/payment.py`, `odoo19/addons/website_sale/models/website.py`, `odoo19/addons/website_sale/models/sale_order.py`
- UI and frontend: `odoo19/addons/website_sale/views/templates.xml`, `odoo19/addons/website_sale/views/website_views.xml`, `odoo19/addons/website_sale/models/product_pricelist.py`
- Tests: `odoo19/addons/website_sale/tests/test_address.py`, `odoo19/addons/website_sale/tests/test_website_sale_pricelist.py`, `odoo19/addons/website_sale/tests/test_website_sale_product_configurator.py`

### Related notes
- `[[docs/Community Addons/sale_management/sale_management|sale_management]]`
- `[[docs/Community Addons/website/website|website]]`

### Risks and follow-up
- Anonymous sessions, multi-company pricelists, taxes, and delivery costs interact in checkout, so storefront bugs often trace back to configuration rather than controller code alone.
- Product configurator and pricing behavior should always be tested with the same website, fiscal position, and visitor state that production users will actually have.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.

