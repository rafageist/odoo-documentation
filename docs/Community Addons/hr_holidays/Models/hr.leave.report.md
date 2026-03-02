<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.report

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/hr_leave_report.py`
- Python classes: `HrLeaveReport`
- Description: Time Off Summary / Report
- Inherits: `hr.manager.department.report`

## Field footprint

- Detected fields: 12
- Field types: `Char` x 1, `Datetime` x 2, `Float` x 2, `Many2one` x 5, `Selection` x 2
- Relation fields: 5

## Sample fields

- `allocation_id`: `Many2one` (comodel `hr.leave.allocation`)
- `company_id`: `Many2one` (comodel `res.company`)
- `date_from`: `Datetime` (comodel `Start Date`)
- `date_to`: `Datetime` (comodel `End Date`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `holiday_status_id`: `Many2one` (comodel `hr.leave.type`)
- `leave_id`: `Many2one` (comodel `hr.leave`)
- `leave_type`: `Selection`
- `name`: `Char` (comodel `Description`)
- `number_of_days`: `Float` (comodel `Number of Days`)
- `number_of_hours`: `Float` (comodel `Number of Hours`)
- `state`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: `action_open_record`
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
title hr.leave.report - Direct Relations
class "hr.leave.report" as hr_leave_report
class "hr.department" as hr_department
class "hr.leave" as hr_leave
class "hr.leave.allocation" as hr_leave_allocation
class "hr.leave.type" as hr_leave_type
class "res.company" as res_company
hr_leave_report --> hr_leave : leave_id
hr_leave_report --> hr_leave_allocation : allocation_id
hr_leave_report --> hr_department : department_id
hr_leave_report --> hr_leave_type : holiday_status_id
hr_leave_report --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Models]]

<!-- GENERATED:MODEL -->
