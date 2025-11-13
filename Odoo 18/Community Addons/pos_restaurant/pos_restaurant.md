<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Restaurant

- Version: v18
- Category: community
- Source: odoo/addons/pos_restaurant
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Restaurant extensions for the Point of Sale 

## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountFiscalPosition`
- `PosConfig`
- `PosOrder`
- `restaurant.floor`
- `restaurant.table`
- `PosSession`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Restaurant - Models and Relations
class AccountFiscalPosition
class PosConfig
class PosOrder
class "restaurant.floor" as restaurant_floor
class "restaurant.table" as restaurant_table
class PosSession
PosConfig .. restaurant_floor : many2many
class "account.fiscal.position" as account_fiscal_position
PosConfig --> account_fiscal_position : many2one
PosOrder --> restaurant_table : many2one
class "pos.config" as pos_config
restaurant_floor .. pos_config : many2many
restaurant_floor --|> restaurant_table : one2many
restaurant_table --> restaurant_floor : many2one
restaurant_table --> restaurant_table : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
