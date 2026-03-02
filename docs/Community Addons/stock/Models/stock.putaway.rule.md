<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.putaway.rule

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_strategy.py`
- Python classes: `StockPutawayRule`
- Description: Putaway Rule

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 6, `Selection` x 1
- Relation fields: 7

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `category_id`: `Many2one` (comodel `product.category`)
- `company_id`: `Many2one` (comodel `res.company`)
- `location_in_id`: `Many2one` (comodel `stock.location`)
- `location_out_id`: `Many2one` (comodel `stock.location`)
- `package_type_ids`: `Many2many` (comodel `stock.package.type`)
- `product_id`: `Many2one` (comodel `product.product`)
- `sequence`: `Integer` (comodel `Priority`)
- `storage_category_id`: `Many2one` (comodel `stock.storage.category`, compute `_compute_storage_category`, store `True`)
- `sublocation`: `Selection`

## Method hints

- Detected methods: 11
- Action methods: none
- Compute methods: `_compute_storage_category`
- Onchange methods: `_onchange_location_in`, `_onchange_sublocation`

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
title stock.putaway.rule - Direct Relations
class "stock.putaway.rule" as stock_putaway_rule
class "product.category" as product_category
class "product.product" as product_product
class "res.company" as res_company
class "stock.location" as stock_location
class "stock.package.type" as stock_package_type
class "stock.storage.category" as stock_storage_category
stock_putaway_rule --> product_product : product_id
stock_putaway_rule --> product_category : category_id
stock_putaway_rule --> stock_location : location_in_id
stock_putaway_rule --> stock_location : location_out_id
stock_putaway_rule --> res_company : company_id
stock_putaway_rule .. stock_package_type : package_type_ids
stock_putaway_rule --> stock_storage_category : storage_category_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
