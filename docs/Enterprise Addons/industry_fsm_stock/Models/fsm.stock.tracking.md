<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# fsm.stock.tracking

- Module: [[docs/Enterprise Addons/industry_fsm_stock/industry_fsm_stock|industry_fsm_stock]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/fsm_stock_tracking.py`
- Python classes: `FsmStockTracking`
- Description: Track Stock

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Many2one` x 3, `One2many` x 2, `Selection` x 1
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `is_same_warehouse`: `Boolean` (compute `_compute_is_same_warehouse`)
- `product_id`: `Many2one` (comodel `product.product`)
- `task_id`: `Many2one` (comodel `project.task`)
- `tracking`: `Selection` (related `product_id.tracking`)
- `tracking_line_ids`: `One2many` (comodel `fsm.stock.tracking.line`)
- `tracking_validated_line_ids`: `One2many` (comodel `fsm.stock.tracking.line`)

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_is_same_warehouse`
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
title fsm.stock.tracking - Direct Relations
class "fsm.stock.tracking" as fsm_stock_tracking
class "fsm.stock.tracking.line" as fsm_stock_tracking_line
class "product.product" as product_product
class "project.task" as project_task
class "res.company" as res_company
fsm_stock_tracking --> project_task : task_id
fsm_stock_tracking --> product_product : product_id
fsm_stock_tracking --|> fsm_stock_tracking_line : tracking_line_ids
fsm_stock_tracking --|> fsm_stock_tracking_line : tracking_validated_line_ids
fsm_stock_tracking --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_stock/Models]]

<!-- GENERATED:MODEL -->
