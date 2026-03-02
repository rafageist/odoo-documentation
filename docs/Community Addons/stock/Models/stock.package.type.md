<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.package.type

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_package_type.py`
- Python classes: `StockPackageType`
- Description: Stock package type

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 1, `Char` x 5, `Float` x 5, `Integer` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `barcode`: `Char` (comodel `Barcode`)
- `base_weight`: `Float`
- `company_id`: `Many2one` (comodel `res.company`)
- `has_quants`: `Boolean` (comodel `Has Contents`, compute `_compute_has_quants`)
- `height`: `Float` (comodel `Height`)
- `length_uom_name`: `Char` (compute `_compute_length_uom_name`)
- `max_weight`: `Float` (comodel `Max Weight`)
- `name`: `Char` (comodel `Package Type`)
- `package_use`: `Selection`
- `packaging_length`: `Float` (comodel `Length`)
- `route_ids`: `Many2many` (comodel `stock.route`)
- `sequence`: `Integer` (comodel `Sequence`)
- `sequence_code`: `Char` (comodel `Sequence Prefix`, related `sequence_id.code`)
- `sequence_id`: `Many2one` (comodel `ir.sequence`)
- `storage_category_capacity_ids`: `One2many` (comodel `stock.storage.category.capacity`)
- `weight_uom_name`: `Char` (compute `_compute_weight_uom_name`)
- `width`: `Float` (comodel `Width`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_has_quants`, `_compute_length_uom_name`, `_compute_weight_uom_name`
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
title stock.package.type - Direct Relations
class "stock.package.type" as stock_package_type
class "ir.sequence" as ir_sequence
class "res.company" as res_company
class "stock.route" as stock_route
class "stock.storage.category.capacity" as stock_storage_category_capacity
stock_package_type --> ir_sequence : sequence_id
stock_package_type --> res_company : company_id
stock_package_type --|> stock_storage_category_capacity : storage_category_capacity_ids
stock_package_type .. stock_route : route_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
