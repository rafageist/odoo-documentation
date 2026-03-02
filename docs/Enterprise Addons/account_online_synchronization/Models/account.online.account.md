<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.online.account

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_online.py`
- Python classes: `AccountOnlineAccount`
- Description: representation of an online bank account

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 2, `Char` x 4, `Date` x 1, `Float` x 2, `Many2one` x 3, `One2many` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `account_data`: `Char`
- `account_number`: `Char`
- `account_online_link_id`: `Many2one` (comodel `account.online.link`)
- `available_balance`: `Float`
- `balance`: `Float`
- `company_id`: `Many2one` (comodel `res.company`, related `account_online_link_id.company_id`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `fetching_status`: `Selection`
- `inverse_balance_sign`: `Boolean`
- `inverse_transaction_sign`: `Boolean`
- `journal_ids`: `One2many` (comodel `account.journal`)
- `last_sync`: `Date` (comodel `Last Transaction Synchronized on`)
- `name`: `Char`
- `online_identifier`: `Char`

## Method hints

- Detected methods: 11
- Action methods: `action_reset_fetching_status`
- Compute methods: none
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
title account.online.account - Direct Relations
class "account.online.account" as account_online_account
class "account.journal" as account_journal
class "account.online.link" as account_online_link
class "res.company" as res_company
class "res.currency" as res_currency
account_online_account --> account_online_link : account_online_link_id
account_online_account --|> account_journal : journal_ids
account_online_account --> res_company : company_id
account_online_account --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Models]]

<!-- GENERATED:MODEL -->
