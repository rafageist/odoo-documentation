<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Coupons, Promotions, Gift Card and Loyalty for eCommerce

- Version: v18
- Category: community
- Source: odoo/addons/website_sale_loyalty
- Dependencies: [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]], [[Odoo 18/Community Addons/website_links/website_links|website_links]], [[Odoo 18/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

## Summary

Use coupon, promotion, gift cards and loyalty programs in your eCommerce store

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `LoyaltyCard`
- `loyalty.program`
- `LoyaltyRule`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Coupons, Promotions, Gift Card and Loyalty for eCommerce - Models and Relations
class LoyaltyCard
class "loyalty.program" as loyalty_program
class LoyaltyRule
class SaleOrder
class SaleOrderLine
class "loyalty.reward" as loyalty_reward
SaleOrder .. loyalty_reward : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
