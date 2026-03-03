<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.message

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/mail_message.py`
- Python classes: `MailMessage`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 1, `Many2one` x 5, `Text` x 1
- Relation fields: 5

## Sample fields

- `account_audit_log_account_id`: `Many2one` (comodel `account.account`, compute `_compute_account_audit_log_account_id`)
- `account_audit_log_company_id`: `Many2one` (comodel `res.company`, compute `_compute_account_audit_log_company_id`)
- `account_audit_log_move_id`: `Many2one` (comodel `account.move`, compute `_compute_account_audit_log_move_id`)
- `account_audit_log_partner_id`: `Many2one` (comodel `res.partner`, compute `_compute_account_audit_log_partner_id`)
- `account_audit_log_preview`: `Text` (compute `_compute_account_audit_log_preview`)
- `account_audit_log_restricted`: `Boolean` (compute `_compute_account_audit_log_restricted`)
- `account_audit_log_tax_id`: `Many2one` (comodel `account.tax`, compute `_compute_account_audit_log_tax_id`)

## Method hints

- Detected methods: 18
- Action methods: none
- Compute methods: `_compute_account_audit_log_account_id`, `_compute_account_audit_log_company_id`, `_compute_account_audit_log_move_id`, `_compute_account_audit_log_partner_id`, `_compute_account_audit_log_preview`, `_compute_account_audit_log_restricted`, `_compute_account_audit_log_tax_id`, `_compute_audit_log_related_record_id`
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
title mail.message - Direct Relations
class "mail.message" as mail_message
class "account.account" as account_account
class "account.move" as account_move
class "account.tax" as account_tax
class "res.company" as res_company
class "res.partner" as res_partner
mail_message --> account_move : account_audit_log_move_id
mail_message --> res_partner : account_audit_log_partner_id
mail_message --> account_account : account_audit_log_account_id
mail_message --> account_tax : account_audit_log_tax_id
mail_message --> res_company : account_audit_log_company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
