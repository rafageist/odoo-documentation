<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.picking.type

- Module: [[docs/Community Addons/repair/repair|repair]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPickingType`

## Field footprint

- Detected fields: 10
- Field types: `Integer` x 4, `Many2one` x 4, `PropertiesDefinition` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `code`: `Selection`
- `count_repair_confirmed`: `Integer` (compute `_compute_count_repair`)
- `count_repair_late`: `Integer` (compute `_compute_count_repair`)
- `count_repair_ready`: `Integer` (compute `_compute_count_repair`)
- `count_repair_under_repair`: `Integer` (compute `_compute_count_repair`)
- `default_product_location_dest_id`: `Many2one` (comodel `stock.location`, compute `_compute_default_product_location_id`, store `True`)
- `default_product_location_src_id`: `Many2one` (comodel `stock.location`, compute `_compute_default_product_location_id`, store `True`)
- `default_recycle_location_dest_id`: `Many2one` (comodel `stock.location`, compute `_compute_default_recycle_location_dest_id`, store `True`)
- `default_remove_location_dest_id`: `Many2one` (comodel `stock.location`, compute `_compute_default_remove_location_dest_id`, store `True`)
- `repair_properties_definition`: `PropertiesDefinition` (comodel `Repair Properties`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_count_repair`, `_compute_default_location_dest_id`, `_compute_default_location_src_id`, `_compute_default_product_location_id`, `_compute_default_recycle_location_dest_id`, `_compute_default_remove_location_dest_id`
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
title stock.picking.type - Direct Relations
class "stock.picking.type" as stock_picking_type
class "stock.location" as stock_location
stock_picking_type --> stock_location : default_product_location_src_id
stock_picking_type --> stock_location : default_product_location_dest_id
stock_picking_type --> stock_location : default_remove_location_dest_id
stock_picking_type --> stock_location : default_recycle_location_dest_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/repair/Models]]

<!-- GENERATED:MODEL -->
