<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# PoS Preparation Display Restaurant

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_restaurant_preparation_display
- Dependencies: [[Odoo 18/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 18/Enterprise Addons/pos_preparation_display/pos_preparation_display|pos_preparation_display]]

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
- `PosPreparationDisplayOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PoS Preparation Display Restaurant - Models and Relations
class PosConfig
class PosPreparationDisplayOrder
class "restaurant.table" as restaurant_table
PosPreparationDisplayOrder --> restaurant_table : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
