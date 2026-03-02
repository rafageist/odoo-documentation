<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move.reversal

- Module: [[docs/Enterprise Addons/helpdesk_account/helpdesk_account|helpdesk_account]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `wizard/account_move_reversal.py`
- Python classes: `AccountMoveReversal`

## Field footprint

- Detected fields: 5
- Field types: `Many2many` x 3, `Many2one` x 2
- Relation fields: 5

## Sample fields

- `helpdesk_sale_order_id`: `Many2one` (comodel `sale.order`)
- `helpdesk_ticket_id`: `Many2one` (comodel `helpdesk.ticket`)
- `move_ids`: `Many2many` (comodel `account.move`, compute `_compute_move_ids`, store `True`)
- `suitable_move_ids`: `Many2many` (comodel `account.move`, compute `_compute_suitable_moves`)
- `suitable_sale_order_ids`: `Many2many` (comodel `sale.order`, compute `_compute_suitable_sale_orders`)

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_journal_id`, `_compute_move_ids`, `_compute_suitable_moves`, `_compute_suitable_sale_orders`
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
class "account.move" as account_move
class "helpdesk.ticket" as helpdesk_ticket
class "sale.order" as sale_order
account_move_reversal .. account_move : move_ids
account_move_reversal --> helpdesk_ticket : helpdesk_ticket_id
account_move_reversal --> sale_order : helpdesk_sale_order_id
account_move_reversal .. account_move : suitable_move_ids
account_move_reversal .. sale_order : suitable_sale_order_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_account/Models]]

<!-- GENERATED:MODEL -->
