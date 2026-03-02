<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Point of Sale enterprise

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/pos_enterprise
- Dependencies: [[Odoo 19/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Advanced features for PoS

## XML Artifacts (detected)

- Views: 12
- Actions: 5
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 9

## Detected Models

- `PosCategory`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `pos.prep.display`
- `pos.prep.line`
- `pos.prep.order`
- `pos.prep.stage`
- `pos.prep.state`
- `PosPreset`
- `PosSession`
- `product.attribute`
- `product.template.attribute.value`
- `product.attribute.custom.value`
- `ProductProduct`
- `ResourceCalendarAttendance`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale enterprise - Models and Relations
class PosCategory
class PosConfig
class PosOrder
class PosOrderLine
class "pos.prep.display" as pos_prep_display
class "pos.prep.line" as pos_prep_line
class "pos.prep.order" as pos_prep_order
class "pos.prep.stage" as pos_prep_stage
class "pos.prep.state" as pos_prep_state
class PosPreset
class PosSession
class "product.attribute" as product_attribute
class "product.template.attribute.value" as product_template_attribute_value
class "product.attribute.custom.value" as product_attribute_custom_value
class ProductProduct
class ResourceCalendarAttendance
class "res.company" as res_company
pos_prep_display --> res_company : many2one
class "pos.config" as pos_config
pos_prep_display .. pos_config : many2many
class "pos.category" as pos_category
pos_prep_display .. pos_category : many2many
pos_prep_display --|> pos_prep_stage : one2many
pos_prep_line --> pos_prep_order : many2one
class "product.product" as product_product
pos_prep_line --> product_product : many2one
pos_prep_line .. product_template_attribute_value : many2many
pos_prep_line --|> pos_prep_line : one2many
pos_prep_line --> pos_prep_line : many2one
class "pos.order.line" as pos_order_line
pos_prep_line --> pos_order_line : many2one
class "pos.order" as pos_order
pos_prep_order --> pos_order : many2one
pos_prep_order --|> pos_prep_line : one2many
pos_prep_stage --> pos_prep_display : many2one
pos_prep_state --> pos_prep_line : many2one
pos_prep_state --> pos_prep_stage : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

