<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.multicurrency.revaluation.wizard

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/multicurrency_revaluation.py`
- Python classes: `AccountMulticurrencyRevaluationWizard`
- Description: Multicurrency Revaluation Wizard

## Field footprint

- Detected fields: 8
- Field types: `Date` x 2, `Many2one` x 5, `Text` x 1
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `date`: `Date`
- `expense_provision_account_id`: `Many2one` (comodel `account.account`, compute `_compute_accounting_values`)
- `income_provision_account_id`: `Many2one` (comodel `account.account`, compute `_compute_accounting_values`)
- `journal_id`: `Many2one` (comodel `account.journal`, compute `_compute_accounting_values`)
- `preview_data`: `Text` (compute `_compute_preview_data`)
- `reversal_date`: `Date`
- `show_warning_move_id`: `Many2one` (comodel `account.move`, compute `_compute_show_warning`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_accounting_values`, `_compute_preview_data`, `_compute_show_warning`
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
title account.multicurrency.revaluation.wizard - Direct Relations
class "account.multicurrency.revaluation.wizard" as account_multicurrency_revaluation_wizard
class "account.account" as account_account
class "account.journal" as account_journal
class "account.move" as account_move
class "res.company" as res_company
account_multicurrency_revaluation_wizard --> res_company : company_id
account_multicurrency_revaluation_wizard --> account_journal : journal_id
account_multicurrency_revaluation_wizard --> account_account : expense_provision_account_id
account_multicurrency_revaluation_wizard --> account_account : income_provision_account_id
account_multicurrency_revaluation_wizard --> account_move : show_warning_move_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Models]]

<!-- GENERATED:MODEL -->
