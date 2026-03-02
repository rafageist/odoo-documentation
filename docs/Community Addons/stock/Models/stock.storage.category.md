<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.storage.category

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_storage_category.py`
- Python classes: `StockStorageCategory`
- Description: Storage Category

## Field footprint

- Detected fields: 9
- Field types: `Char` x 2, `Float` x 1, `Many2one` x 1, `One2many` x 4, `Selection` x 1
- Relation fields: 5

## Sample fields

- `allow_new_product`: `Selection`
- `capacity_ids`: `One2many` (comodel `stock.storage.category.capacity`)
- `company_id`: `Many2one` (comodel `res.company`)
- `location_ids`: `One2many` (comodel `stock.location`)
- `max_weight`: `Float` (comodel `Max Weight`)
- `name`: `Char` (comodel `Storage Category`)
- `package_capacity_ids`: `One2many` (comodel `stock.storage.category.capacity`, compute `_compute_storage_capacity_ids`)
- `product_capacity_ids`: `One2many` (comodel `stock.storage.category.capacity`, compute `_compute_storage_capacity_ids`)
- `weight_uom_name`: `Char` (compute `_compute_weight_uom_name`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_storage_capacity_ids`, `_compute_weight_uom_name`
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
title stock.storage.category - Direct Relations
class "stock.storage.category" as stock_storage_category
class "res.company" as res_company
class "stock.location" as stock_location
class "stock.storage.category.capacity" as stock_storage_category_capacity
stock_storage_category --|> stock_storage_category_capacity : capacity_ids
stock_storage_category --|> stock_storage_category_capacity : product_capacity_ids
stock_storage_category --|> stock_storage_category_capacity : package_capacity_ids
stock_storage_category --|> stock_location : location_ids
stock_storage_category --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
