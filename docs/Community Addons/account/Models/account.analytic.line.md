<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.analytic.line

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_analytic_line.py`
- Python classes: `AccountAnalyticLine`
- Description: Analytic Line

## Field footprint

- Detected fields: 8
- Field types: `Char` x 2, `Many2one` x 5, `Selection` x 1
- Relation fields: 5

## Sample fields

- `category`: `Selection`
- `code`: `Char`
- `general_account_id`: `Many2one` (comodel `account.account`, compute `_compute_general_account_id`, store `True`)
- `journal_id`: `Many2one` (comodel `account.journal`, related `move_line_id.journal_id`, store `True`)
- `move_line_id`: `Many2one` (comodel `account.move.line`)
- `partner_id`: `Many2one` (compute `_compute_partner_id`, store `True`)
- `product_id`: `Many2one` (comodel `product.product`)
- `ref`: `Char`

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_general_account_id`, `_compute_partner_id`
- Onchange methods: `on_change_unit_amount`

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
title account.analytic.line - Direct Relations
class "account.analytic.line" as account_analytic_line
class "account.account" as account_account
class "account.journal" as account_journal
class "account.move.line" as account_move_line
class "product.product" as product_product
account_analytic_line --> product_product : product_id
account_analytic_line --> account_account : general_account_id
account_analytic_line --> account_journal : journal_id
account_analytic_line --> account_move_line : move_line_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
