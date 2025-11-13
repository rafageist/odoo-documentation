<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Quality Base

- Version: v19
- Category: enterprise
- Source: enterprise19/quality
- Dependencies: [[Odoo 19/Community Addons/stock/stock|stock]]

## Summary

Basic Feature for Quality

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 4
- Access CSV entries: 20

## Detected Models

- `quality.point.test_type`
- `quality.point`
- `quality.alert.team`
- `quality.reason`
- `quality.tag`
- `quality.alert.stage`
- `quality.check`
- `quality.alert`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Quality Base - Models and Relations
class "quality.point.test_type" as quality_point_test_type
class "quality.point" as quality_point
class "quality.alert.team" as quality_alert_team
class "quality.reason" as quality_reason
class "quality.tag" as quality_tag
class "quality.alert.stage" as quality_alert_stage
class "quality.check" as quality_check
class "quality.alert" as quality_alert
quality_point --> quality_alert_team : many2one
class "product.product" as product_product
quality_point .. product_product : many2many
class "product.category" as product_category
quality_point .. product_category : many2many
class "stock.picking.type" as stock_picking_type
quality_point .. stock_picking_type : many2many
class "res.company" as res_company
quality_point --> res_company : many2one
class "res.users" as res_users
quality_point --> res_users : many2one
quality_point --|> quality_check : one2many
quality_point --> quality_point_test_type : many2one
class "stock.location" as stock_location
quality_point .. stock_location : many2many
quality_alert_team --> res_company : many2one
quality_alert_stage .. quality_alert_team : many2many
quality_check --> quality_point : many2one
quality_check --> product_product : many2one
class "stock.picking" as stock_picking
quality_check --> stock_picking : many2one
class "stock.lot" as stock_lot
quality_check .. stock_lot : many2many
quality_check --> res_users : many2one
quality_check --> quality_alert_team : many2one
quality_check --> res_company : many2one
quality_check --|> quality_alert : one2many
quality_check --> quality_point_test_type : many2one
quality_check --> stock_location : many2one
quality_alert --> quality_alert_stage : many2one
quality_alert --> res_company : many2one
quality_alert --> quality_reason : many2one
quality_alert .. quality_tag : many2many
quality_alert --> stock_picking : many2one
quality_alert --> res_users : many2one
quality_alert --> quality_alert_team : many2one
class "res.partner" as res_partner
quality_alert --> res_partner : many2one
quality_alert --> quality_check : many2one
class "product.template" as product_template
quality_alert --> product_template : many2one
quality_alert --> product_product : many2one
quality_alert .. stock_lot : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
