<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS Self Order

- Scope: Community Addons
- Source: odoo/addons/pos_self_order
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Community Addons/http_routing/http_routing|http_routing]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]]

## Summary

Addon for the POS App that allows customers to view the menu on their smartphone.

## XML Artifacts (detected)

- Views: 12
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `mail.template`
- `PosCategory`
- `PosConfig`
- `PosOrderLine`
- `PosOrder`
- `PosPaymentMethod`
- `PosPreset`
- `RestaurantTable`
- `RestaurantFloor`
- `pos_self_order.custom_link`
- `PosSession`
- `ProductTemplate`
- `ProductProduct`
- `ProductTag`
- `res.country`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title POS Self Order - Models and Relations
class "mail.template" as mail_template
class PosCategory
class PosConfig
class PosOrderLine
class PosOrder
class PosPaymentMethod
class PosPreset
class RestaurantTable
class RestaurantFloor
class "pos_self_order.custom_link" as pos_self_order_custom_link
class PosSession
class ProductTemplate
class ProductProduct
class ProductTag
class "res.country" as res_country
class ResPartner
class "pos.config" as pos_config
PosCategory .. pos_config : many2many
class "res.lang" as res_lang
PosConfig --> res_lang : many2one
PosConfig .. res_lang : many2many
class "ir.attachment" as ir_attachment
PosConfig .. ir_attachment : many2many
PosConfig .. ir_attachment : many2many
class "res.users" as res_users
PosConfig --> res_users : many2one
class "product.combo" as product_combo
PosOrderLine --> product_combo : many2one
class "restaurant.table" as restaurant_table
PosOrder --> restaurant_table : many2one
PosPreset --> mail_template : many2one
pos_self_order_custom_link .. pos_config : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





