<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Coupons & Loyalty

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/loyalty
- Dependencies: [[Odoo 19/Community Addons/product/product|product]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/account/account|account]]

## Summary

Use discounts, gift card, eWallets and loyalty programs in different sales channels

## XML Artifacts (detected)

- Views: 16
- Actions: 10
- Menus: 0
- Rules (ir.rule): 5
- Access CSV entries: 8

## Detected Models

- `loyalty.card`
- `loyalty.history`
- `loyalty.mail`
- `loyalty.program`
- `loyalty.reward`
- `loyalty.rule`
- `ProductPricelist`
- `ProductProduct`
- `ProductTemplate`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Coupons & Loyalty - Models and Relations
class "loyalty.card" as loyalty_card
class "loyalty.history" as loyalty_history
class "loyalty.mail" as loyalty_mail
class "loyalty.program" as loyalty_program
class "loyalty.reward" as loyalty_reward
class "loyalty.rule" as loyalty_rule
class ProductPricelist
class ProductProduct
class ProductTemplate
class ResPartner
loyalty_card --> loyalty_program : many2one
class "res.partner" as res_partner
loyalty_card --> res_partner : many2one
loyalty_card --|> loyalty_history : one2many
loyalty_history --> loyalty_card : many2one
loyalty_mail --> loyalty_program : many2one
class "mail.template" as mail_template
loyalty_mail --> mail_template : many2one
class "res.company" as res_company
loyalty_program --> res_company : many2one
class "res.currency" as res_currency
loyalty_program --> res_currency : many2one
class "product.pricelist" as product_pricelist
loyalty_program .. product_pricelist : many2many
loyalty_program --|> loyalty_rule : one2many
loyalty_program --|> loyalty_reward : one2many
loyalty_program --|> loyalty_mail : one2many
loyalty_program --> mail_template : many2one
loyalty_program --|> loyalty_card : one2many
class "product.product" as product_product
loyalty_program --> product_product : many2one
loyalty_reward --> loyalty_program : many2one
loyalty_reward .. product_product : many2many
class "product.category" as product_category
loyalty_reward --> product_category : many2one
class "product.tag" as product_tag
loyalty_reward --> product_tag : many2one
loyalty_reward .. product_product : many2many
loyalty_reward --> product_product : many2one
loyalty_reward --> product_product : many2one
loyalty_reward --> product_tag : many2one
loyalty_reward .. product_product : many2many
class "uom.uom" as uom_uom
loyalty_reward --> uom_uom : many2one
loyalty_rule --> loyalty_program : many2one
loyalty_rule .. product_product : many2many
loyalty_rule --> product_category : many2one
loyalty_rule --> product_tag : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


