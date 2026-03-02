<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.loan

- Module: [[docs/Enterprise Addons/account_loans/account_loans|account_loans]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_loan.py`
- Python classes: `AccountLoan`
- Description: Loan
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 28
- Field types: `Boolean` x 2, `Char` x 2, `Date` x 4, `Integer` x 4, `Many2one` x 7, `Monetary` x 5, `One2many` x 2, `Properties` x 1, `Selection` x 1
- Relation fields: 9

## Sample fields

- `active`: `Boolean`
- `amount_borrowed`: `Monetary`
- `amount_borrowed_difference`: `Monetary` (compute `_compute_amount_borrowed_difference`)
- `asset_group_id`: `Many2one` (comodel `account.asset.group`)
- `company_id`: `Many2one` (comodel `res.company`)
- `count_linked_assets`: `Integer` (compute `_compute_linked_assets`)
- `currency_id`: `Many2one` (related `company_id.currency_id`)
- `date`: `Date` (comodel `Loan Date`)
- `display_name`: `Char` (store `True`)
- `duration`: `Integer` (comodel `Duration`)
- `duration_difference`: `Integer` (compute `_compute_duration_difference`)
- `end_date`: `Date` (compute `_compute_start_end_date`)
- `expense_account_id`: `Many2one` (comodel `account.account`)
- `interest`: `Monetary`
- `interest_difference`: `Monetary` (compute `_compute_interest_difference`)
- `is_wrong_date`: `Boolean` (compute `_compute_is_wrong_date`)
- `journal_id`: `Many2one` (comodel `account.journal`)
- `line_ids`: `One2many` (comodel `account.loan.line`)
- `linked_assets_ids`: `One2many` (comodel `account.asset`, compute `_compute_linked_assets`)
- `loan_properties`: `Properties` (comodel `Properties`)

## Method hints

- Detected methods: 22
- Action methods: `action_cancel`, `action_close`, `action_confirm`, `action_file_uploaded`, `action_open_compute_wizard`, `action_open_linked_assets`, `action_open_loan_entries`, `action_reset`, and 2 more
- Compute methods: `_compute_amount_borrowed_difference`, `_compute_display_name`, `_compute_duration_difference`, `_compute_interest_difference`, `_compute_is_wrong_date`, `_compute_linked_assets`, `_compute_nb_posted_entries`, `_compute_outstanding_balance`, and 1 more
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
title account.loan - Direct Relations
class "account.loan" as account_loan
class "account.account" as account_account
class "account.asset" as account_asset
class "account.asset.group" as account_asset_group
class "account.journal" as account_journal
class "account.loan.line" as account_loan_line
class "res.company" as res_company
account_loan --> res_company : company_id
account_loan --> account_account : long_term_account_id
account_loan --> account_account : short_term_account_id
account_loan --> account_account : expense_account_id
account_loan --> account_journal : journal_id
account_loan --> account_asset_group : asset_group_id
account_loan --|> account_loan_line : line_ids
account_loan --|> account_asset : linked_assets_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_loans/Models]]

<!-- GENERATED:MODEL -->
