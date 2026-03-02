<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.category

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductCategory`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Many2many` x 3, `Many2one` x 1, `One2many` x 1, `Selection` x 1
- Relation fields: 5

## Sample fields

- `filter_for_stock_putaway_rule`: `Boolean` (comodel `stock.putaway.rule`, store `False`)
- `packaging_reserve_method`: `Selection`
- `parent_route_ids`: `Many2many` (comodel `stock.route`, compute `_compute_parent_route_ids`)
- `putaway_rule_ids`: `One2many` (comodel `stock.putaway.rule`)
- `removal_strategy_id`: `Many2one` (comodel `product.removal`)
- `route_ids`: `Many2many` (comodel `stock.route`)
- `total_route_ids`: `Many2many` (comodel `stock.route`, compute `_compute_total_route_ids`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_parent_route_ids`, `_compute_total_route_ids`
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
title product.category - Direct Relations
class "product.category" as product_category
class "product.removal" as product_removal
class "stock.putaway.rule" as stock_putaway_rule
class "stock.route" as stock_route
product_category .. stock_route : route_ids
product_category --> product_removal : removal_strategy_id
product_category .. stock_route : parent_route_ids
product_category .. stock_route : total_route_ids
product_category --|> stock_putaway_rule : putaway_rule_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
