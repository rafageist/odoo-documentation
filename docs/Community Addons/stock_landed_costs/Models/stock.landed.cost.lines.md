<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.landed.cost.lines

- Module: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_landed_cost.py`
- Python classes: `StockLandedCostLines`
- Description: Stock Landed Cost Line

## Field footprint

- Detected fields: 7
- Field types: `Char` x 1, `Many2one` x 4, `Monetary` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `account_id`: `Many2one` (comodel `account.account`)
- `cost_id`: `Many2one` (comodel `stock.landed.cost`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `cost_id.currency_id`)
- `name`: `Char` (comodel `Description`)
- `price_unit`: `Monetary` (comodel `Cost`)
- `product_id`: `Many2one` (comodel `product.product`)
- `split_method`: `Selection`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
- Onchange methods: `onchange_product_id`

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
title stock.landed.cost.lines - Direct Relations
class "stock.landed.cost.lines" as stock_landed_cost_lines
class "account.account" as account_account
class "product.product" as product_product
class "res.currency" as res_currency
class "stock.landed.cost" as stock_landed_cost
stock_landed_cost_lines --> stock_landed_cost : cost_id
stock_landed_cost_lines --> product_product : product_id
stock_landed_cost_lines --> account_account : account_id
stock_landed_cost_lines --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_landed_costs/Models]]

<!-- GENERATED:MODEL -->
