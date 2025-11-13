<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# MRP II

- Version: v18
- Category: enterprise
- Source: enterprise18/mrp_workorder
- Dependencies: [[Odoo 18/Enterprise Addons/quality/quality|quality]], [[Odoo 18/Community Addons/mrp/mrp|mrp]], [[Odoo 18/Community Addons/barcodes/barcodes|barcodes]], [[Odoo 18/Enterprise Addons/web_gantt/web_gantt|web_gantt]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/hr_hourly_cost/hr_hourly_cost|hr_hourly_cost]]

## Summary

Work Orders, Planning, Stock Reports.

## XML Artifacts (detected)

- Views: 36
- Actions: 19
- Menus: 6
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `mrp.bom`
- `MrpProduction`
- `MrpWorkcenter`
- `MrpWorkcenterProductivity`
- `mrp.workorder`
- `TestType`
- `MrpRouting`
- `QualityPoint`
- `QualityAlert`
- `QualityCheck`
- `StockMove`
- `StockMoveLine`
- `PickingType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MRP II - Models and Relations
class HrEmployee
class "mrp.bom" as mrp_bom
class MrpProduction
class MrpWorkcenter
class MrpWorkcenterProductivity
class "mrp.workorder" as mrp_workorder
class TestType
class MrpRouting
class QualityPoint
class QualityAlert
class QualityCheck
class StockMove
class StockMoveLine
class PickingType
class "quality.check" as quality_check
MrpProduction --|> quality_check : one2many
class "hr.employee" as hr_employee
MrpProduction .. hr_employee : many2many
MrpWorkcenter .. hr_employee : many2many
MrpWorkcenterProductivity --> hr_employee : many2one
class "quality.point" as quality_point
mrp_workorder .. quality_point : many2many
mrp_workorder --|> quality_check : one2many
mrp_workorder .. quality_check : many2many
mrp_workorder .. quality_check : many2many
class "quality.alert" as quality_alert
mrp_workorder --|> quality_alert : one2many
mrp_workorder --> quality_check : many2one
class "quality.point.test_type" as quality_point_test_type
mrp_workorder --> quality_point_test_type : many2one
mrp_workorder --> hr_employee : many2one
mrp_workorder .. hr_employee : many2many
mrp_workorder .. hr_employee : many2many
mrp_workorder .. hr_employee : many2many
MrpRouting --|> quality_point : one2many
class "mrp.routing.workcenter" as mrp_routing_workcenter
QualityPoint --> mrp_routing_workcenter : many2one
class "product.product" as product_product
QualityPoint --|> product_product : one2many
QualityPoint --|> product_product : one2many
QualityPoint --> quality_point_test_type : many2one
QualityPoint --> product_product : many2one
QualityAlert --> mrp_workorder : many2one
class "mrp.workcenter" as mrp_workcenter
QualityAlert --> mrp_workcenter : many2one
class "mrp.production" as mrp_production
QualityAlert --> mrp_production : many2one
QualityCheck --> mrp_workorder : many2one
QualityCheck --> mrp_workcenter : many2one
QualityCheck --> mrp_production : many2one
QualityCheck --> quality_check : many2one
QualityCheck --> quality_check : many2one
class "stock.move" as stock_move
QualityCheck --> stock_move : many2one
class "stock.move.line" as stock_move_line
QualityCheck --> stock_move_line : many2one
QualityCheck --> product_product : many2one
class "uom.uom" as uom_uom
QualityCheck --> uom_uom : many2one
class "stock.lot" as stock_lot
QualityCheck --> stock_lot : many2one
QualityCheck --> hr_employee : many2one
StockMoveLine --|> quality_check : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
