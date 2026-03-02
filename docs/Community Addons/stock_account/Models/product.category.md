<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.category

- Module: [[docs/Community Addons/stock_account/stock_account|stock_account]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductCategory`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Many2one` x 3, `Selection` x 2
- Relation fields: 3

## Sample fields

- `anglo_saxon_accounting`: `Boolean` (compute `_compute_anglo_saxon_accounting`)
- `property_cost_method`: `Selection`
- `property_price_difference_account_id`: `Many2one` (comodel `account.account`)
- `property_stock_journal`: `Many2one` (comodel `account.journal`)
- `property_stock_valuation_account_id`: `Many2one` (comodel `account.account`)
- `property_valuation`: `Selection`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_anglo_saxon_accounting`
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
class "account.account" as account_account
class "account.journal" as account_journal
product_category --> account_journal : property_stock_journal
product_category --> account_account : property_stock_valuation_account_id
product_category --> account_account : property_price_difference_account_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock_account/Models]]

<!-- GENERATED:MODEL -->
