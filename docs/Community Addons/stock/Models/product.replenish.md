<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.replenish

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/product_replenish.py`
- Python classes: `ProductReplenish`
- Description: Product Replenish
- Inherits: `stock.replenish.mixin`

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 1, `Datetime` x 1, `Float` x 2, `Many2many` x 1, `Many2one` x 6
- Relation fields: 7

## Sample fields

- `allowed_uom_ids`: `Many2many` (comodel `uom.uom`, compute `_compute_allowed_uom_ids`)
- `company_id`: `Many2one` (comodel `res.company`)
- `date_planned`: `Datetime` (comodel `Scheduled Date`, compute `_compute_date_planned`, store `True`)
- `forecast_uom_id`: `Many2one` (related `product_id.uom_id`)
- `forecasted_quantity`: `Float` (compute `_compute_forecasted_quantity`)
- `product_has_variants`: `Boolean` (comodel `Has variants`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_tmpl_id`: `Many2one` (comodel `product.template`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`)
- `quantity`: `Float` (comodel `Quantity`)
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_allowed_uom_ids`, `_compute_date_planned`, `_compute_forecasted_quantity`
- Onchange methods: `_onchange_product_id`

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
title product.replenish - Direct Relations
class "product.replenish" as product_replenish
class "product.product" as product_product
class "product.template" as product_template
class "res.company" as res_company
class "stock.warehouse" as stock_warehouse
class "uom.uom" as uom_uom
product_replenish --> product_product : product_id
product_replenish --> product_template : product_tmpl_id
product_replenish .. uom_uom : allowed_uom_ids
product_replenish --> uom_uom : product_uom_id
product_replenish --> stock_warehouse : warehouse_id
product_replenish --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
