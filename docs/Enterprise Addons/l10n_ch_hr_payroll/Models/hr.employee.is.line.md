<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.employee.is.line

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_employee_is_line.py`
- Python classes: `HrEmployeeIsLine`
- Description: IS Entry / Withdrawals / Mutations

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 1, `Many2one` x 1, `One2many` x 3, `Selection` x 3
- Relation fields: 5

## Sample fields

- `active`: `Boolean`
- `correction_method`: `Selection`
- `correction_type`: `Selection`
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `is_ema_ids`: `One2many` (comodel `l10n.ch.is.mutation`)
- `is_log_line_ids`: `One2many` (comodel `hr.payslip.is.log.line`)
- `manual_correction_ids`: `One2many` (comodel `hr.employee.is.line.correction`)
- `payslips_to_correct`: `Many2many` (comodel `hr.payslip`)
- `reason`: `Char`
- `state`: `Selection`

## Method hints

- Detected methods: 4
- Action methods: `action_done`, `action_draft`, `action_pending`
- Compute methods: `_compute_display_name`
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
title hr.employee.is.line - Direct Relations
class "hr.employee.is.line" as hr_employee_is_line
class "hr.employee" as hr_employee
class "hr.employee.is.line.correction" as hr_employee_is_line_correction
class "hr.payslip" as hr_payslip
class "hr.payslip.is.log.line" as hr_payslip_is_log_line
class "l10n.ch.is.mutation" as l10n_ch_is_mutation
hr_employee_is_line --> hr_employee : employee_id
hr_employee_is_line .. hr_payslip : payslips_to_correct
hr_employee_is_line --|> l10n_ch_is_mutation : is_ema_ids
hr_employee_is_line --|> hr_employee_is_line_correction : manual_correction_ids
hr_employee_is_line --|> hr_payslip_is_log_line : is_log_line_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
