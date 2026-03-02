<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Delivery Costs

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/delivery
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/payment_custom/payment_custom|payment_custom]]

## XML Artifacts (detected)

- Views: 12
- Actions: 2
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 10

## Detected Models

- `delivery.carrier`
- `delivery.price.rule`
- `delivery.zip.prefix`
- `ir.module.module`
- `PaymentProvider`
- `PaymentTransaction`
- `ProductCategory`
- `ResPartner`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Delivery Costs - Models and Relations
class "delivery.carrier" as delivery_carrier
class "delivery.price.rule" as delivery_price_rule
class "delivery.zip.prefix" as delivery_zip_prefix
class "ir.module.module" as ir_module_module
class PaymentProvider
class PaymentTransaction
class ProductCategory
class ResPartner
class SaleOrder
class SaleOrderLine
class "res.company" as res_company
delivery_carrier --> res_company : many2one
class "product.product" as product_product
delivery_carrier --> product_product : many2one
class "res.country" as res_country
delivery_carrier .. res_country : many2many
class "res.country.state" as res_country_state
delivery_carrier .. res_country_state : many2many
delivery_carrier .. delivery_zip_prefix : many2many
class "product.tag" as product_tag
delivery_carrier .. product_tag : many2many
delivery_carrier .. product_tag : many2many
delivery_carrier --|> delivery_price_rule : one2many
delivery_price_rule --> delivery_carrier : many2one
ResPartner --> delivery_carrier : many2one
SaleOrder --> delivery_carrier : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


