<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.allocation.generate.multi.wizard

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/hr_leave_allocation_generate_multi_wizard.py`
- Python classes: `HrLeaveAllocationGenerateMultiWizard`
- Description: Generate time off allocations for multiple employees

## Field footprint

- Detected fields: 14
- Field types: `Char` x 1, `Date` x 2, `Float` x 1, `Many2many` x 1, `Many2one` x 5, `Selection` x 3, `Text` x 1
- Relation fields: 6

## Sample fields

- `accrual_plan_id`: `Many2one` (comodel `hr.leave.accrual.plan`)
- `allocation_mode`: `Selection`
- `allocation_type`: `Selection`
- `category_id`: `Many2one` (comodel `hr.employee.category`)
- `company_id`: `Many2one` (comodel `res.company`)
- `date_from`: `Date` (comodel `Start Date`)
- `date_to`: `Date` (comodel `End Date`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `duration`: `Float`
- `employee_ids`: `Many2many` (comodel `hr.employee`)
- `holiday_status_id`: `Many2one` (comodel `hr.leave.type`)
- `name`: `Char` (comodel `Description`, compute `_compute_name`, store `True`)
- `notes`: `Text` (comodel `Reasons`)
- `request_unit`: `Selection` (related `holiday_status_id.request_unit`)

## Method hints

- Detected methods: 7
- Action methods: `action_generate_allocations`
- Compute methods: `_compute_name`
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
title hr.leave.allocation.generate.multi.wizard - Direct Relations
class "hr.leave.allocation.generate.multi.wizard" as hr_leave_allocation_generate_multi_wizard
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.employee.category" as hr_employee_category
class "hr.leave.accrual.plan" as hr_leave_accrual_plan
class "hr.leave.type" as hr_leave_type
class "res.company" as res_company
hr_leave_allocation_generate_multi_wizard --> hr_leave_type : holiday_status_id
hr_leave_allocation_generate_multi_wizard .. hr_employee : employee_ids
hr_leave_allocation_generate_multi_wizard --> res_company : company_id
hr_leave_allocation_generate_multi_wizard --> hr_department : department_id
hr_leave_allocation_generate_multi_wizard --> hr_employee_category : category_id
hr_leave_allocation_generate_multi_wizard --> hr_leave_accrual_plan : accrual_plan_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Models]]

<!-- GENERATED:MODEL -->
