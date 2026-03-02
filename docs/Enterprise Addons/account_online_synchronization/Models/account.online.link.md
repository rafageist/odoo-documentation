<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.online.link

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_online.py`
- Python classes: `AccountOnlineLink`
- Description: Bank Connection
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 3, `Char` x 6, `Date` x 1, `Datetime` x 2, `Json` x 1, `Many2one` x 1, `One2many` x 2, `Selection` x 1
- Relation fields: 3

## Sample fields

- `access_token`: `Char`
- `account_online_account_ids`: `One2many` (comodel `account.online.account`)
- `auto_sync`: `Boolean`
- `client_id`: `Char`
- `company_id`: `Many2one` (comodel `res.company`)
- `connection_state_details`: `Json`
- `expiring_synchronization_date`: `Date`
- `has_unlinked_accounts`: `Boolean`
- `journal_ids`: `One2many` (comodel `account.journal`, compute `_compute_journal_ids`)
- `last_refresh`: `Datetime`
- `name`: `Char`
- `next_refresh`: `Datetime` (comodel `Next synchronization`, compute `_compute_next_synchronization`)
- `provider_type`: `Char`
- `refresh_token`: `Char`
- `renewal_contact_email`: `Char`
- `show_sync_actions`: `Boolean` (compute `_compute_show_sync_actions`)
- `state`: `Selection`

## Method hints

- Detected methods: 38
- Action methods: `action_fetch_transactions`, `action_new_synchronization`, `action_reconnect_account`, `action_update_credentials`
- Compute methods: `_compute_journal_ids`, `_compute_next_synchronization`, `_compute_show_sync_actions`
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
title account.online.link - Direct Relations
class "account.online.link" as account_online_link
class "account.journal" as account_journal
class "account.online.account" as account_online_account
class "res.company" as res_company
account_online_link --|> account_online_account : account_online_account_ids
account_online_link --> res_company : company_id
account_online_link --|> account_journal : journal_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Models]]

<!-- GENERATED:MODEL -->
