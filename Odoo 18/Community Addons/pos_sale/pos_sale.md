<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# POS - Sales

- Version: v18
- Category: community
- Source: odoo/addons/pos_sale
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Link module between Point of Sale and Sales

## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `CrmTeam`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`
- `ProductProduct`
- `sale.order`
- `sale.order.line`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS - Sales - Models and Relations
class CrmTeam
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class ProductProduct
class "sale.order" as sale_order
class "sale.order.line" as sale_order_line
class StockPicking
class "pos.config" as pos_config
CrmTeam --|> pos_config : one2many
class "crm.team" as crm_team
PosConfig --> crm_team : many2one
class "product.product" as product_product
PosConfig --> product_product : many2one
PosOrder --> crm_team : many2one
PosOrderLine --> sale_order : many2one
PosOrderLine --> sale_order_line : many2one
PosSession --> crm_team : many2one
class "pos.order.line" as pos_order_line
sale_order --|> pos_order_line : one2many
sale_order_line --|> pos_order_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
