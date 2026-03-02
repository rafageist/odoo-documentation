<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 2, `Datetime` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 5, `Selection` x 1
- Relation fields: 6

## Sample fields

- `account_display_representative_field`: `Boolean` (compute `_compute_account_display_representative_field`)
- `account_last_return_cron_refresh`: `Datetime`
- `account_representative_id`: `Many2one` (comodel `res.partner`)
- `account_return_periodicity`: `Selection`
- `account_return_reminder_day`: `Integer`
- `account_revaluation_expense_provision_account_id`: `Many2one` (comodel `account.account`)
- `account_revaluation_income_provision_account_id`: `Many2one` (comodel `account.account`)
- `account_revaluation_journal_id`: `Many2one` (comodel `account.journal`)
- `account_tax_return_journal_id`: `Many2one` (comodel `account.journal`)
- `account_tax_unit_ids`: `Many2many` (comodel `account.tax.unit`)
- `totals_below_sections`: `Boolean` (compute `_compute_totals_below_sections`, store `True`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_account_display_representative_field`, `_compute_totals_below_sections`
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
title res.company - Direct Relations
class "res.company" as res_company
class "account.account" as account_account
class "account.journal" as account_journal
class "account.tax.unit" as account_tax_unit
class "res.partner" as res_partner
res_company --> account_journal : account_tax_return_journal_id
res_company --> account_journal : account_revaluation_journal_id
res_company --> account_account : account_revaluation_expense_provision_account_id
res_company --> account_account : account_revaluation_income_provision_account_id
res_company .. account_tax_unit : account_tax_unit_ids
res_company --> res_partner : account_representative_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Models]]

<!-- GENERATED:MODEL -->
