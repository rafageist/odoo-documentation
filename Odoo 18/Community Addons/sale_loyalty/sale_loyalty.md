<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sale Loyalty

- Version: v18
- Category: community
- Source: odoo/addons/sale_loyalty
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Community Addons/loyalty/loyalty|loyalty]]

## Summary

Use discounts and loyalty programs in sales orders

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 17

## Detected Models

- `LoyaltyCard`
- `LoyaltyHistory`
- `LoyaltyProgram`
- `LoyaltyReward`
- `SaleOrder`
- `sale.order.coupon.points`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale Loyalty - Models and Relations
class LoyaltyCard
class LoyaltyHistory
class LoyaltyProgram
class LoyaltyReward
class SaleOrder
class "sale.order.coupon.points" as sale_order_coupon_points
class SaleOrderLine
class "sale.order" as sale_order
LoyaltyCard --> sale_order : many2one
class "loyalty.card" as loyalty_card
SaleOrder .. loyalty_card : many2many
class "loyalty.rule" as loyalty_rule
SaleOrder .. loyalty_rule : many2many
SaleOrder --|> sale_order_coupon_points : one2many
sale_order_coupon_points --> sale_order : many2one
sale_order_coupon_points --> loyalty_card : many2one
class "loyalty.reward" as loyalty_reward
SaleOrderLine --> loyalty_reward : many2one
SaleOrderLine --> loyalty_card : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
