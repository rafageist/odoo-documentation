<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# POS Self Order

- Version: v18
- Category: community
- Source: odoo/addons/pos_self_order
- Dependencies: [[Odoo 18/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 18/Community Addons/http_routing/http_routing|http_routing]]

## Summary

Addon for the POS App that allows customers to view the menu on their smartphone.

## XML Artifacts (detected)

- Views: 11
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountFiscalPosition`
- `PosCategory`
- `PosConfig`
- `PosOrderLine`
- `PosOrder`
- `PosPaymentMethod`
- `RestaurantTable`
- `RestaurantFloor`
- `pos_self_order.custom_link`
- `PosSession`
- `ProductTemplate`
- `ProductProduct`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS Self Order - Models and Relations
class AccountFiscalPosition
class PosCategory
class PosConfig
class PosOrderLine
class PosOrder
class PosPaymentMethod
class RestaurantTable
class RestaurantFloor
class "pos_self_order.custom_link" as pos_self_order_custom_link
class PosSession
class ProductTemplate
class ProductProduct
class "res.lang" as res_lang
PosConfig --> res_lang : many2one
PosConfig .. res_lang : many2many
class "ir.attachment" as ir_attachment
PosConfig .. ir_attachment : many2many
class "res.users" as res_users
PosConfig --> res_users : many2one
class "product.combo" as product_combo
PosOrderLine --> product_combo : many2one
class "pos.config" as pos_config
pos_self_order_custom_link .. pos_config : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
