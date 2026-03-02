<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_au.payslip.ytd

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_account/l10n_au_hr_payroll_account|l10n_au_hr_payroll_account]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_au_payslip_ytd.py`
- Python classes: `L10n_AuPayslipYtd`
- Description: YTD Opening Balances

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 2, `Char` x 2, `Date` x 1, `Float` x 1, `Many2one` x 5, `Monetary` x 1, `One2many` x 1, `Selection` x 1
- Relation fields: 6

## Sample fields

- `code`: `Char` (related `rule_id.code`)
- `company_id`: `Many2one` (related `employee_id.company_id`)
- `currency_id`: `Many2one` (related `company_id.currency_id`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `finalised`: `Boolean`
- `l10n_au_income_stream_type`: `Selection`
- `l10n_au_payslip_ytd_input_ids`: `One2many` (comodel `l10n_au.payslip.ytd.input`)
- `name`: `Char` (compute `_compute_name`)
- `requires_inputs`: `Boolean` (comodel `Requires Inputs`)
- `rule_id`: `Many2one` (comodel `hr.salary.rule`)
- `start_date`: `Date`
- `start_value`: `Monetary`
- `struct_id`: `Many2one` (comodel `hr.payroll.structure`, compute `_compute_struct_id`, store `True`)
- `ytd_amount`: `Float` (compute `_compute_total_ytd`)

## Method hints

- Detected methods: 12
- Action methods: `action_add_inputs`
- Compute methods: `_compute_name`, `_compute_struct_id`, `_compute_total_ytd`
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
title l10n_au.payslip.ytd - Direct Relations
class "l10n_au.payslip.ytd" as l10n_au_payslip_ytd
class "hr.employee" as hr_employee
class "hr.payroll.structure" as hr_payroll_structure
class "hr.salary.rule" as hr_salary_rule
class "l10n_au.payslip.ytd.input" as l10n_au_payslip_ytd_input
l10n_au_payslip_ytd --> hr_employee : employee_id
l10n_au_payslip_ytd --> hr_payroll_structure : struct_id
l10n_au_payslip_ytd --> hr_salary_rule : rule_id
l10n_au_payslip_ytd --|> l10n_au_payslip_ytd_input : l10n_au_payslip_ytd_input_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_account/Models]]

<!-- GENERATED:MODEL -->
