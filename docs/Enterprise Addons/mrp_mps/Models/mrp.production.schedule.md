<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# mrp.production.schedule

- Module: [[docs/Enterprise Addons/mrp_mps/mrp_mps|mrp_mps]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/mrp_mps.py`
- Python classes: `MrpProductionSchedule`
- Description: Schedule the production of Product in a warehouse
- Inherits: `stock.replenish.mixin`

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Float` x 2, `Integer` x 1, `Many2one` x 9, `One2many` x 1, `Selection` x 2
- Relation fields: 10

## Sample fields

- `bom_id`: `Many2one` (comodel `mrp.bom`)
- `company_id`: `Many2one` (comodel `res.company`)
- `forecast_ids`: `One2many` (comodel `mrp.product.forecast`)
- `forecast_target_qty`: `Float` (comodel `Safety Stock Target`)
- `is_indirect`: `Boolean` (comodel `Indirect demand product`)
- `is_manufacture_route`: `Boolean` (compute `_compute_is_manufacture_route`)
- `min_to_replenish_qty`: `Float` (comodel `Minimum to Replenish`)
- `mps_sequence`: `Integer` (comodel `Sequence`)
- `product_category_id`: `Many2one` (comodel `product.category`, related `product_id.product_tmpl_id.categ_id`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_tmpl_id`: `Many2one` (comodel `product.template`, related `product_id.product_tmpl_id`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`, related `product_id.uom_id`)
- `replenish_state`: `Selection` (store `False`)
- `replenish_trigger`: `Selection`
- `route_id`: `Many2one` (compute `_compute_route_and_supplier`, store `True`)
- `supplier_id`: `Many2one` (compute `_compute_route_and_supplier`, store `True`)
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`)

## Method hints

- Detected methods: 37
- Action methods: `action_cron_replenish`, `action_open_actual_demand_details`, `action_open_actual_replenishment_details`, `action_replenish`, `action_toggle_is_indirect`
- Compute methods: `_compute_is_manufacture_route`, `_compute_route_and_supplier`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title mrp.production.schedule - Direct Relations
class "mrp.production.schedule" as mrp_production_schedule
class "mrp.bom" as mrp_bom
class "mrp.product.forecast" as mrp_product_forecast
class "product.category" as product_category
class "product.product" as product_product
class "product.template" as product_template
class "res.company" as res_company
class "stock.warehouse" as stock_warehouse
class "uom.uom" as uom_uom
mrp_production_schedule --|> mrp_product_forecast : forecast_ids
mrp_production_schedule --> res_company : company_id
mrp_production_schedule --> product_product : product_id
mrp_production_schedule --> product_template : product_tmpl_id
mrp_production_schedule --> product_category : product_category_id
mrp_production_schedule --> uom_uom : product_uom_id
mrp_production_schedule --> stock_warehouse : warehouse_id
mrp_production_schedule --> mrp_bom : bom_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_mps/Models]]

<!-- GENERATED:MODEL -->
