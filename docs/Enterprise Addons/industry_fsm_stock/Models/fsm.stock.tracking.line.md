<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# fsm.stock.tracking.line

- Module: [[docs/Enterprise Addons/industry_fsm_stock/industry_fsm_stock|industry_fsm_stock]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/fsm_stock_tracking.py`
- Python classes: `FsmStockTrackingLine`
- Description: Lines for FSM Stock Tracking

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Float` x 1, `Many2one` x 7
- Relation fields: 7

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `is_same_warehouse`: `Boolean` (compute `_compute_warehouse`)
- `lot_id`: `Many2one` (comodel `stock.lot`)
- `product_id`: `Many2one` (comodel `product.product`)
- `quantity`: `Float`
- `sale_order_line_id`: `Many2one` (comodel `sale.order.line`)
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`, compute `_compute_warehouse`)
- `wizard_tracking_line`: `Many2one` (comodel `fsm.stock.tracking`)
- `wizard_tracking_line_validated`: `Many2one` (comodel `fsm.stock.tracking`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_warehouse`
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
title fsm.stock.tracking.line - Direct Relations
class "fsm.stock.tracking.line" as fsm_stock_tracking_line
class "fsm.stock.tracking" as fsm_stock_tracking
class "product.product" as product_product
class "res.company" as res_company
class "sale.order.line" as sale_order_line
class "stock.lot" as stock_lot
class "stock.warehouse" as stock_warehouse
fsm_stock_tracking_line --> stock_lot : lot_id
fsm_stock_tracking_line --> product_product : product_id
fsm_stock_tracking_line --> sale_order_line : sale_order_line_id
fsm_stock_tracking_line --> res_company : company_id
fsm_stock_tracking_line --> fsm_stock_tracking : wizard_tracking_line
fsm_stock_tracking_line --> fsm_stock_tracking : wizard_tracking_line_validated
fsm_stock_tracking_line --> stock_warehouse : warehouse_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_stock/Models]]

<!-- GENERATED:MODEL -->
