<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Restaurant

- Scope: Community Addons
- Source: odoo/addons/pos_restaurant
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Restaurant extensions for the Point of Sale 

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosPayment`
- `PosPreset`
- `restaurant.floor`
- `restaurant.table`
- `PosSession`
- `restaurant.order.course`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Restaurant - Models and Relations
class PosConfig
class PosOrder
class PosOrderLine
class PosPayment
class PosPreset
class "restaurant.floor" as restaurant_floor
class "restaurant.table" as restaurant_table
class PosSession
class "restaurant.order.course" as restaurant_order_course
PosConfig .. restaurant_floor : many2many
PosOrder --> restaurant_table : many2one
PosOrder --|> restaurant_order_course : one2many
PosOrderLine --> restaurant_order_course : many2one
class "pos.config" as pos_config
restaurant_floor .. pos_config : many2many
restaurant_floor --|> restaurant_table : one2many
restaurant_table --> restaurant_floor : many2one
restaurant_table --> restaurant_table : many2one
class "pos.order" as pos_order
restaurant_order_course --> pos_order : many2one
class "pos.order.line" as pos_order_line
restaurant_order_course --|> pos_order_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





