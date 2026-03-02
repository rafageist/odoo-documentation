<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# PoS Preparation Display Restaurant

- Scope: Enterprise Addons
- Source: enterprise/pos_restaurant_preparation_display
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



