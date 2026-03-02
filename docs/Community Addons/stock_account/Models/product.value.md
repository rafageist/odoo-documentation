<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.value

- Module: [[docs/Community Addons/stock_account/stock_account|stock_account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/product_value.py`
- Python classes: `ProductValue`
- Description: Product Value

## Field footprint

- Detected fields: 13
- Field types: `Char` x 2, `Datetime` x 1, `Many2one` x 6, `Monetary` x 2, `Text` x 2
- Relation fields: 6

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`, compute `_compute_company_id`, store `True`)
- `computed_value_description`: `Text` (compute `_compute_value_description`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `company_id.currency_id`)
- `current_value`: `Monetary` (related `move_id.value`)
- `current_value_description`: `Text` (compute `_compute_value_description`)
- `current_value_details`: `Char` (compute `_compute_current_value_details`)
- `date`: `Datetime`
- `description`: `Char`
- `lot_id`: `Many2one` (comodel `stock.lot`)
- `move_id`: `Many2one` (comodel `stock.move`)
- `product_id`: `Many2one` (comodel `product.product`)
- `user_id`: `Many2one` (comodel `res.users`)
- `value`: `Monetary`

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_company_id`, `_compute_current_value_details`, `_compute_value_description`
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
title product.value - Direct Relations
class "product.value" as product_value
class "product.product" as product_product
class "res.company" as res_company
class "res.currency" as res_currency
class "res.users" as res_users
class "stock.lot" as stock_lot
class "stock.move" as stock_move
product_value --> product_product : product_id
product_value --> stock_lot : lot_id
product_value --> stock_move : move_id
product_value --> res_company : company_id
product_value --> res_currency : currency_id
product_value --> res_users : user_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_account/Models]]

<!-- GENERATED:MODEL -->
