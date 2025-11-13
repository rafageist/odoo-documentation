<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Point of Sale - Coupons & Loyalty

- Version: v19
- Category: community
- Source: odoo19/addons/pos_loyalty
- Dependencies: [[Odoo 19/Community Addons/loyalty/loyalty|loyalty]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Use Coupons, Gift Cards and Loyalty programs in Point of Sale

## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 13

## Detected Models

- `BarcodeRule`
- `loyalty.card`
- `LoyaltyMail`
- `loyalty.program`
- `loyalty.reward`
- `loyalty.rule`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`
- `ProductProduct`
- `ProductTemplate`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale - Coupons & Loyalty - Models and Relations
class BarcodeRule
class "loyalty.card" as loyalty_card
class LoyaltyMail
class "loyalty.program" as loyalty_program
class "loyalty.reward" as loyalty_reward
class "loyalty.rule" as loyalty_rule
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class ProductProduct
class ProductTemplate
class ResPartner
class "pos.order" as pos_order
loyalty_card --> pos_order : many2one
class "res.partner" as res_partner
loyalty_card --> res_partner : many2one
class "ir.actions.report" as ir_actions_report
LoyaltyMail --> ir_actions_report : many2one
class "pos.config" as pos_config
loyalty_program .. pos_config : many2many
loyalty_program --> ir_actions_report : many2one
class "product.product" as product_product
loyalty_rule .. product_product : many2many
PosOrderLine --> loyalty_reward : many2one
PosOrderLine --> loyalty_card : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
