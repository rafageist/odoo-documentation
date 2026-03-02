<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.landed.cost

- Module: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_landed_cost.py`
- Python classes: `StockLandedCost`
- Description: Stock Landed Cost
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 14
- Field types: `Char` x 1, `Date` x 1, `Many2many` x 1, `Many2one` x 5, `Monetary` x 1, `One2many` x 2, `Selection` x 2, `Text` x 1
- Relation fields: 8

## Sample fields

- `account_journal_id`: `Many2one` (comodel `account.journal`)
- `account_move_id`: `Many2one` (comodel `account.move`)
- `amount_total`: `Monetary` (comodel `Total`, compute `_compute_total_amount`, store `True`)
- `company_id`: `Many2one` (comodel `res.company`)
- `cost_lines`: `One2many` (comodel `stock.landed.cost.lines`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `company_id.currency_id`)
- `date`: `Date` (comodel `Date`)
- `description`: `Text` (comodel `Item Description`)
- `name`: `Char` (comodel `Name`)
- `picking_ids`: `Many2many` (comodel `stock.picking`)
- `state`: `Selection`
- `target_model`: `Selection`
- `valuation_adjustment_lines`: `One2many` (comodel `stock.valuation.adjustment.lines`)
- `vendor_bill_id`: `Many2one` (comodel `account.move`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_total_amount`
- Onchange methods: `_onchange_target_model`

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
title stock.landed.cost - Direct Relations
class "stock.landed.cost" as stock_landed_cost
class "account.journal" as account_journal
class "account.move" as account_move
class "res.company" as res_company
class "res.currency" as res_currency
class "stock.landed.cost.lines" as stock_landed_cost_lines
class "stock.picking" as stock_picking
class "stock.valuation.adjustment.lines" as stock_valuation_adjustment_lines
stock_landed_cost .. stock_picking : picking_ids
stock_landed_cost --|> stock_landed_cost_lines : cost_lines
stock_landed_cost --|> stock_valuation_adjustment_lines : valuation_adjustment_lines
stock_landed_cost --> account_move : account_move_id
stock_landed_cost --> account_journal : account_journal_id
stock_landed_cost --> res_company : company_id
stock_landed_cost --> account_move : vendor_bill_id
stock_landed_cost --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_landed_costs/Models]]

<!-- GENERATED:MODEL -->
