<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.warehouse

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_warehouse.py`
- Python classes: `StockWarehouse`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `subcontracting_mto_pull_id`: `Many2one` (comodel `stock.rule`)
- `subcontracting_pull_id`: `Many2one` (comodel `stock.rule`)
- `subcontracting_resupply_type_id`: `Many2one` (comodel `stock.picking.type`)
- `subcontracting_route_id`: `Many2one` (comodel `stock.route`)
- `subcontracting_to_resupply`: `Boolean` (comodel `Resupply Subcontractors`)
- `subcontracting_type_id`: `Many2one` (comodel `stock.picking.type`)

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: none
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
class "stock.picking.type" as stock_picking_type
class "stock.route" as stock_route
class "stock.rule" as stock_rule
stock_warehouse --> stock_rule : subcontracting_mto_pull_id
stock_warehouse --> stock_rule : subcontracting_pull_id
stock_warehouse --> stock_route : subcontracting_route_id
stock_warehouse --> stock_picking_type : subcontracting_type_id
stock_warehouse --> stock_picking_type : subcontracting_resupply_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Models]]

<!-- GENERATED:MODEL -->
