<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.payroll.alloc.paid.leave

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_payroll_allocating_paid_time_off.py`
- Python classes: `HrPayrollAllocPaidLeave`
- Description: Manage the Allocation of Paid Time Off

## Field footprint

- Detected fields: 7
- Field types: `Many2many` x 1, `Many2one` x 4, `One2many` x 1, `Selection` x 1
- Relation fields: 6

## Sample fields

- `alloc_employee_ids`: `One2many` (comodel `hr.payroll.alloc.employee`, compute `_compute_alloc_employee_ids`)
- `company_id`: `Many2one` (comodel `res.company`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_ids`: `Many2many` (comodel `hr.employee`)
- `holiday_status_id`: `Many2one` (comodel `hr.leave.type`)
- `structure_type_id`: `Many2one` (comodel `hr.payroll.structure.type`)
- `year`: `Selection`

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_alloc_employee_ids`
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
title hr.payroll.alloc.paid.leave - Direct Relations
class "hr.payroll.alloc.paid.leave" as hr_payroll_alloc_paid_leave
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.leave.type" as hr_leave_type
class "hr.payroll.alloc.employee" as hr_payroll_alloc_employee
class "hr.payroll.structure.type" as hr_payroll_structure_type
class "res.company" as res_company
hr_payroll_alloc_paid_leave --> hr_payroll_structure_type : structure_type_id
hr_payroll_alloc_paid_leave .. hr_employee : employee_ids
hr_payroll_alloc_paid_leave --|> hr_payroll_alloc_employee : alloc_employee_ids
hr_payroll_alloc_paid_leave --> hr_leave_type : holiday_status_id
hr_payroll_alloc_paid_leave --> res_company : company_id
hr_payroll_alloc_paid_leave --> hr_department : department_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
