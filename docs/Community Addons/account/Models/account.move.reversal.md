<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move.reversal

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/account_move_reversal.py`
- Python classes: `AccountMoveReversal`
- Description: Account Move Reversal

## Field footprint

- Detected fields: 11
- Field types: `Char` x 3, `Date` x 1, `Many2many` x 3, `Many2one` x 3, `Monetary` x 1
- Relation fields: 6

## Sample fields

- `available_journal_ids`: `Many2many` (comodel `account.journal`, compute `_compute_available_journal_ids`)
- `company_id`: `Many2one` (comodel `res.company`)
- `country_code`: `Char` (related `company_id.country_id.code`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_from_moves`)
- `date`: `Date`
- `journal_id`: `Many2one` (comodel `account.journal`, compute `_compute_journal_id`, store `True`)
- `move_ids`: `Many2many` (comodel `account.move`)
- `move_type`: `Char` (compute `_compute_from_moves`)
- `new_move_ids`: `Many2many` (comodel `account.move`)
- `reason`: `Char`
- `residual`: `Monetary` (compute `_compute_from_moves`)

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_available_journal_ids`, `_compute_from_moves`, `_compute_journal_id`
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
title account.move.reversal - Direct Relations
class "account.move.reversal" as account_move_reversal
class "account.journal" as account_journal
class "account.move" as account_move
class "res.company" as res_company
class "res.currency" as res_currency
account_move_reversal .. account_move : move_ids
account_move_reversal .. account_move : new_move_ids
account_move_reversal --> account_journal : journal_id
account_move_reversal --> res_company : company_id
account_move_reversal .. account_journal : available_journal_ids
account_move_reversal --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
