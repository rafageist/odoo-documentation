<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.valuation.adjustment.lines

- Module: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_landed_cost.py`
- Python classes: `StockValuationAdjustmentLines`
- Description: Valuation Adjustment Lines

## Field footprint

- Detected fields: 12
- Field types: `Char` x 1, `Float` x 3, `Many2one` x 5, `Monetary` x 3
- Relation fields: 5

## Sample fields

- `additional_landed_cost`: `Monetary` (comodel `Additional Landed Cost`)
- `cost_id`: `Many2one` (comodel `stock.landed.cost`)
- `cost_line_id`: `Many2one` (comodel `stock.landed.cost.lines`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `cost_id.company_id.currency_id`)
- `final_cost`: `Monetary` (comodel `New Value`, compute `_compute_final_cost`, store `True`)
- `former_cost`: `Monetary` (comodel `Original Value`)
- `move_id`: `Many2one` (comodel `stock.move`)
- `name`: `Char` (comodel `Description`, compute `_compute_name`, store `True`)
- `product_id`: `Many2one` (comodel `product.product`)
- `quantity`: `Float` (comodel `Quantity`)
- `volume`: `Float` (comodel `Volume`)
- `weight`: `Float` (comodel `Weight`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_final_cost`, `_compute_name`
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
title stock.valuation.adjustment.lines - Direct Relations
class "stock.valuation.adjustment.lines" as stock_valuation_adjustment_lines
class "product.product" as product_product
class "res.currency" as res_currency
class "stock.landed.cost" as stock_landed_cost
class "stock.landed.cost.lines" as stock_landed_cost_lines
class "stock.move" as stock_move
stock_valuation_adjustment_lines --> stock_landed_cost : cost_id
stock_valuation_adjustment_lines --> stock_landed_cost_lines : cost_line_id
stock_valuation_adjustment_lines --> stock_move : move_id
stock_valuation_adjustment_lines --> product_product : product_id
stock_valuation_adjustment_lines --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_landed_costs/Models]]

<!-- GENERATED:MODEL -->
