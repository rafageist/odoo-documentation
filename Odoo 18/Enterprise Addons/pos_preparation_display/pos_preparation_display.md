<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# PoS Preparation Display

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_preparation_display
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Display Orders for Preparation stage.

## XML Artifacts (detected)

- Views: 5
- Actions: 4
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 8

## Detected Models

- `PosOrder`
- `PosSession`
- `pos_preparation_display.display`
- `pos_preparation_display.order`
- `pos_preparation_display.orderline`
- `pos_preparation_display.order.stage`
- `pos_preparation_display.stage`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PoS Preparation Display - Models and Relations
class PosOrder
class PosSession
class "pos_preparation_display.display" as pos_preparation_display_display
class "pos_preparation_display.order" as pos_preparation_display_order
class "pos_preparation_display.orderline" as pos_preparation_display_orderline
class "pos_preparation_display.order.stage" as pos_preparation_display_order_stage
class "pos_preparation_display.stage" as pos_preparation_display_stage
class "res.company" as res_company
pos_preparation_display_display --> res_company : many2one
class "pos.config" as pos_config
pos_preparation_display_display .. pos_config : many2many
class "pos.category" as pos_category
pos_preparation_display_display .. pos_category : many2many
pos_preparation_display_display --|> pos_preparation_display_stage : one2many
class "pos.order" as pos_order
pos_preparation_display_order --> pos_order : many2one
pos_preparation_display_order --|> pos_preparation_display_order_stage : one2many
pos_preparation_display_order --|> pos_preparation_display_orderline : one2many
class "product.template.attribute.value" as product_template_attribute_value
pos_preparation_display_orderline .. product_template_attribute_value : many2many
class "product.product" as product_product
pos_preparation_display_orderline --> product_product : many2one
pos_preparation_display_orderline --> pos_preparation_display_order : many2one
pos_preparation_display_order_stage --> pos_preparation_display_stage : many2one
pos_preparation_display_order_stage --> pos_preparation_display_display : many2one
pos_preparation_display_order_stage --> pos_preparation_display_order : many2one
pos_preparation_display_stage --> pos_preparation_display_display : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
