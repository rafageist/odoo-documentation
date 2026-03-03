<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.bank.statement.line

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/account_bank_statement_line.py`
- Python classes: `AccountBankStatementLine`
- Description: Bank Statement Line

## Field footprint

- Detected fields: 25
- Field types: `Boolean` x 3, `Char` x 7, `Float` x 1, `Integer` x 1, `Json` x 1, `Many2many` x 1, `Many2one` x 7, `Monetary` x 4
- Relation fields: 8

## Sample fields

- `account_number`: `Char`
- `amount`: `Monetary`
- `amount_currency`: `Monetary` (compute `_compute_amount_currency`, store `True`)
- `amount_residual`: `Float` (compute `_compute_is_reconciled`, store `True`)
- `company_id`: `Many2one` (comodel `res.company`, related `move_id.company_id`, store `True`)
- `country_code`: `Char` (related `company_id.account_fiscal_country_id.code`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_currency_id`, store `True`)
- `foreign_currency_id`: `Many2one` (comodel `res.currency`)
- `internal_index`: `Char` (compute `_compute_internal_index`, store `True`)
- `is_reconciled`: `Boolean` (compute `_compute_is_reconciled`, store `True`)
- `journal_id`: `Many2one` (comodel `account.journal`, related `move_id.journal_id`, store `True`)
- `move_id`: `Many2one` (comodel `account.move`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `partner_name`: `Char`
- `payment_ids`: `Many2many` (comodel `account.payment`)
- `payment_ref`: `Char`
- `running_balance`: `Monetary` (compute `_compute_running_balance`)
- `sequence`: `Integer`
- `statement_balance_end_real`: `Monetary` (related `statement_id.balance_end_real`)
- `statement_complete`: `Boolean` (related `statement_id.is_complete`)

## Method hints

- Detected methods: 23
- Action methods: `action_undo_reconciliation`
- Compute methods: `_compute_amount_currency`, `_compute_currency_id`, `_compute_internal_index`, `_compute_is_reconciled`, `_compute_running_balance`
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
title account.bank.statement.line - Direct Relations
class "account.bank.statement.line" as account_bank_statement_line
class "account.bank.statement" as account_bank_statement
class "account.journal" as account_journal
class "account.move" as account_move
class "account.payment" as account_payment
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
account_bank_statement_line --> account_move : move_id
account_bank_statement_line --> account_journal : journal_id
account_bank_statement_line --> res_company : company_id
account_bank_statement_line --> account_bank_statement : statement_id
account_bank_statement_line .. account_payment : payment_ids
account_bank_statement_line --> res_partner : partner_id
account_bank_statement_line --> res_currency : currency_id
account_bank_statement_line --> res_currency : foreign_currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
