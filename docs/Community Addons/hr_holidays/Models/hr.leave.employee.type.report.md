<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.employee.type.report

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/hr_leave_employee_type_report.py`
- Python classes: `HrLeaveEmployeeTypeReport`
- Description: Time Off Summary / Report

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 1, `Datetime` x 2, `Float` x 2, `Many2one` x 4, `Selection` x 2
- Relation fields: 4

## Sample fields

- `active_employee`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`)
- `date_from`: `Datetime` (comodel `Start Date`)
- `date_to`: `Datetime` (comodel `End Date`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `holiday_status`: `Selection`
- `leave_type`: `Many2one` (comodel `hr.leave.type`)
- `number_of_days`: `Float` (comodel `Number of Days`)
- `number_of_hours`: `Float` (comodel `Number of Hours`)
- `state`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: `action_time_off_analysis`
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
title hr.leave.employee.type.report - Direct Relations
class "hr.leave.employee.type.report" as hr_leave_employee_type_report
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.leave.type" as hr_leave_type
class "res.company" as res_company
hr_leave_employee_type_report --> hr_employee : employee_id
hr_leave_employee_type_report --> hr_department : department_id
hr_leave_employee_type_report --> hr_leave_type : leave_type
hr_leave_employee_type_report --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Models]]

<!-- GENERATED:MODEL -->
