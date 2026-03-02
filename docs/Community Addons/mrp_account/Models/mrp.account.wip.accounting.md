<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mrp.account.wip.accounting

- Module: [[docs/Community Addons/mrp_account/mrp_account|mrp_account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/mrp_wip_accounting.py`
- Python classes: `MrpAccountWipAccounting`
- Description: Wizard to post Manufacturing WIP account move

## Field footprint

- Detected fields: 6
- Field types: `Char` x 1, `Date` x 2, `Many2many` x 1, `Many2one` x 1, `One2many` x 1
- Relation fields: 3

## Sample fields

- `date`: `Date` (comodel `Date`)
- `journal_id`: `Many2one` (comodel `account.journal`)
- `line_ids`: `One2many` (comodel `mrp.account.wip.accounting.line`, compute `_compute_line_ids`, store `True`)
- `mo_ids`: `Many2many` (comodel `mrp.production`)
- `reference`: `Char` (comodel `Reference`)
- `reversal_date`: `Date` (comodel `Reversal Date`, compute `_compute_reversal_date`, store `True`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_line_ids`, `_compute_reversal_date`
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
title mrp.account.wip.accounting - Direct Relations
class "mrp.account.wip.accounting" as mrp_account_wip_accounting
class "account.journal" as account_journal
class "mrp.account.wip.accounting.line" as mrp_account_wip_accounting_line
class "mrp.production" as mrp_production
mrp_account_wip_accounting --> account_journal : journal_id
mrp_account_wip_accounting --|> mrp_account_wip_accounting_line : line_ids
mrp_account_wip_accounting .. mrp_production : mo_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp_account/Models]]

<!-- GENERATED:MODEL -->
