<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.auto.reconcile.wizard

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/account_auto_reconcile_wizard.py`
- Python classes: `AccountAutoReconcileWizard`
- Description: Account automatic reconciliation wizard

## Field footprint

- Detected fields: 7
- Field types: `Date` x 2, `Many2many` x 3, `Many2one` x 1, `Selection` x 1
- Relation fields: 4

## Sample fields

- `account_ids`: `Many2many` (comodel `account.account`)
- `company_id`: `Many2one` (comodel `res.company`)
- `from_date`: `Date`
- `line_ids`: `Many2many` (comodel `account.move.line`)
- `partner_ids`: `Many2many` (comodel `res.partner`)
- `search_mode`: `Selection`
- `to_date`: `Date`

## Method hints

- Detected methods: 7
- Action methods: none
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
title account.auto.reconcile.wizard - Direct Relations
class "account.auto.reconcile.wizard" as account_auto_reconcile_wizard
class "account.account" as account_account
class "account.move.line" as account_move_line
class "res.company" as res_company
class "res.partner" as res_partner
account_auto_reconcile_wizard --> res_company : company_id
account_auto_reconcile_wizard .. account_move_line : line_ids
account_auto_reconcile_wizard .. account_account : account_ids
account_auto_reconcile_wizard .. res_partner : partner_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Models]]

<!-- GENERATED:MODEL -->
