<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_au.previous.payroll.transfer

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/l10n_au_previous_payroll_transfer.py`
- Python classes: `L10n_AuPreviousPayrollTransfer`
- Description: Transfer From Previous Payroll System

## Field footprint

- Detected fields: 4
- Field types: `Char` x 1, `Date` x 1, `Many2one` x 1, `One2many` x 1
- Relation fields: 2

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `fiscal_year_start_date`: `Date`
- `l10n_au_previous_payroll_transfer_employee_ids`: `One2many` (comodel `l10n_au.previous.payroll.transfer.employee`, compute `_compute_all_employees`, store `True`)
- `previous_bms_id`: `Char`

## Method hints

- Detected methods: 4
- Action methods: `action_transfer`
- Compute methods: `_compute_all_employees`
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
title l10n_au.previous.payroll.transfer - Direct Relations
class "l10n_au.previous.payroll.transfer" as l10n_au_previous_payroll_transfer
class "l10n_au.previous.payroll.transfer.employee" as l10n_au_previous_payroll_transfer_employee
class "res.company" as res_company
l10n_au_previous_payroll_transfer --> res_company : company_id
l10n_au_previous_payroll_transfer --|> l10n_au_previous_payroll_transfer_employee : l10n_au_previous_payroll_transfer_employee_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Models]]

<!-- GENERATED:MODEL -->
