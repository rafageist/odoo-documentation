<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Coupons, Promotions, Gift Card and Loyalty for eCommerce

- Scope: Community Addons
- Source: odoo/addons/website_sale_loyalty
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Community Addons/website_links/website_links|website_links]], [[docs/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

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
- `ProductProduct`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Coupons, Promotions, Gift Card and Loyalty for eCommerce - Models and Relations
class LoyaltyCard
class "loyalty.program" as loyalty_program
class LoyaltyRule
class ProductProduct
class SaleOrder
class SaleOrderLine
class "loyalty.reward" as loyalty_reward
SaleOrder .. loyalty_reward : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



