<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payslip.input

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_payslip_input.py`
- Python classes: `HrPayslipInput`
- Description: Payslip Input

## Field footprint

- Detected fields: 10
- Field types: `Char` x 2, `Date` x 1, `Float` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 4
- Relation fields: 5

## Sample fields

- `_allowed_input_type_ids`: `Many2many` (comodel `hr.payslip.input.type`, related `payslip_id.struct_id.input_line_type_ids`)
- `amount`: `Float`
- `code`: `Char` (related `input_type_id.code`)
- `date_from`: `Date` (related `payslip_id.date_from`)
- `employee_id`: `Many2one` (comodel `hr.employee`, related `payslip_id.employee_id`)
- `input_type_id`: `Many2one` (comodel `hr.payslip.input.type`)
- `name`: `Char`
- `payslip_id`: `Many2one` (comodel `hr.payslip`)
- `sequence`: `Integer`
- `version_id`: `Many2one` (related `payslip_id.version_id`)

## Method hints

- Detected methods: 0
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
title hr.payslip.input - Direct Relations
class "hr.payslip.input" as hr_payslip_input
class "hr.employee" as hr_employee
class "hr.payslip" as hr_payslip
class "hr.payslip.input.type" as hr_payslip_input_type
hr_payslip_input --> hr_payslip : payslip_id
hr_payslip_input --> hr_employee : employee_id
hr_payslip_input --> hr_payslip_input_type : input_type_id
hr_payslip_input .. hr_payslip_input_type : _allowed_input_type_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
