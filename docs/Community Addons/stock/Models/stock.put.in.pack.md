<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.put.in.pack

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_put_in_pack.py`
- Python classes: `StockPutInPack`
- Description: Put In Pack Wizard

## Field footprint

- Detected fields: 7
- Field types: `Many2many` x 3, `Many2one` x 4
- Relation fields: 7

## Sample fields

- `location_dest_id`: `Many2one` (comodel `stock.location`)
- `move_line_ids`: `Many2many` (comodel `stock.move.line`)
- `origin_package_ids`: `Many2many` (comodel `stock.package`, compute `_compute_origin_package_ids`)
- `package_ids`: `Many2many` (comodel `stock.package`)
- `package_type_id`: `Many2one` (comodel `stock.package.type`)
- `package_type_sequence_id`: `Many2one` (related `package_type_id.sequence_id`)
- `result_package_id`: `Many2one` (comodel `stock.package`)

## Method hints

- Detected methods: 4
- Action methods: `action_put_in_pack`
- Compute methods: `_compute_origin_package_ids`
- Onchange methods: `_onchange_package_type_id`

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
title stock.put.in.pack - Direct Relations
class "stock.put.in.pack" as stock_put_in_pack
class "stock.location" as stock_location
class "stock.move.line" as stock_move_line
class "stock.package" as stock_package
class "stock.package.type" as stock_package_type
stock_put_in_pack --> stock_location : location_dest_id
stock_put_in_pack .. stock_move_line : move_line_ids
stock_put_in_pack .. stock_package : package_ids
stock_put_in_pack --> stock_package_type : package_type_id
stock_put_in_pack --> stock_package : result_package_id
stock_put_in_pack .. stock_package : origin_package_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
