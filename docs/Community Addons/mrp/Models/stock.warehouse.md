<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.warehouse

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_warehouse.py`
- Python classes: `StockWarehouse`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 1, `Many2one` x 10, `Selection` x 1
- Relation fields: 10

## Sample fields

- `manu_type_id`: `Many2one` (comodel `stock.picking.type`)
- `manufacture_mto_pull_id`: `Many2one` (comodel `stock.rule`)
- `manufacture_pull_id`: `Many2one` (comodel `stock.rule`)
- `manufacture_steps`: `Selection`
- `manufacture_to_resupply`: `Boolean` (comodel `Manufacture to Resupply`, compute `_compute_manufacture_to_resupply`)
- `pbm_loc_id`: `Many2one` (comodel `stock.location`)
- `pbm_mto_pull_id`: `Many2one` (comodel `stock.rule`)
- `pbm_route_id`: `Many2one` (comodel `stock.route`)
- `pbm_type_id`: `Many2one` (comodel `stock.picking.type`)
- `sam_loc_id`: `Many2one` (comodel `stock.location`)
- `sam_rule_id`: `Many2one` (comodel `stock.rule`)
- `sam_type_id`: `Many2one` (comodel `stock.picking.type`)

## Method hints

- Detected methods: 17
- Action methods: none
- Compute methods: `_compute_manufacture_to_resupply`
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
title stock.warehouse - Direct Relations
class "stock.warehouse" as stock_warehouse
class "stock.location" as stock_location
class "stock.picking.type" as stock_picking_type
class "stock.route" as stock_route
class "stock.rule" as stock_rule
stock_warehouse --> stock_rule : manufacture_pull_id
stock_warehouse --> stock_rule : manufacture_mto_pull_id
stock_warehouse --> stock_rule : pbm_mto_pull_id
stock_warehouse --> stock_rule : sam_rule_id
stock_warehouse --> stock_picking_type : manu_type_id
stock_warehouse --> stock_picking_type : pbm_type_id
stock_warehouse --> stock_picking_type : sam_type_id
stock_warehouse --> stock_route : pbm_route_id
stock_warehouse --> stock_location : pbm_loc_id
stock_warehouse --> stock_location : sam_loc_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
