<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.add.to.wave

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_add_to_wave.py`
- Python classes: `StockAddToWave`
- Description: Wave Transfer Lines

## Field footprint

- Detected fields: 5
- Field types: `Many2many` x 2, `Many2one` x 2, `Selection` x 1
- Relation fields: 4

## Sample fields

- `line_ids`: `Many2many` (comodel `stock.move.line`)
- `mode`: `Selection`
- `picking_ids`: `Many2many` (comodel `stock.picking`)
- `user_id`: `Many2one` (comodel `res.users`)
- `wave_id`: `Many2one` (comodel `stock.picking.batch`)

## Method hints

- Detected methods: 2
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
title stock.add.to.wave - Direct Relations
class "stock.add.to.wave" as stock_add_to_wave
class "res.users" as res_users
class "stock.move.line" as stock_move_line
class "stock.picking" as stock_picking
class "stock.picking.batch" as stock_picking_batch
stock_add_to_wave --> stock_picking_batch : wave_id
stock_add_to_wave .. stock_picking : picking_ids
stock_add_to_wave .. stock_move_line : line_ids
stock_add_to_wave --> res_users : user_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Models]]

<!-- GENERATED:MODEL -->
