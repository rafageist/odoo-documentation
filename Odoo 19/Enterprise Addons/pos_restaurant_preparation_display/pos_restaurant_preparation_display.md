<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# PoS Preparation Display Restaurant

- Version: v19
- Category: enterprise
- Source: enterprise19/pos_restaurant_preparation_display
- Dependencies: [[Odoo 19/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 19/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]

## Summary

Display Orders for Preparation stage.

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosOrder`
- `PosPrepDisplay`
- `PosPrepOrder`
- `RestaurantOrderCourse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PoS Preparation Display Restaurant - Models and Relations
class PosConfig
class PosOrder
class PosPrepDisplay
class PosPrepOrder
class RestaurantOrderCourse
class "restaurant.order.course" as restaurant_order_course
PosPrepOrder --> restaurant_order_course : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
