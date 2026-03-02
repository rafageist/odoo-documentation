<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.mandatory.day

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_leave_mandatory_day.py`
- Python classes: `HrLeaveMandatoryDay`
- Description: Mandatory Day

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Date` x 2, `Integer` x 1, `Many2many` x 2, `Many2one` x 2
- Relation fields: 4

## Sample fields

- `color`: `Integer`
- `company_id`: `Many2one` (comodel `res.company`)
- `department_ids`: `Many2many` (comodel `hr.department`)
- `end_date`: `Date`
- `job_ids`: `Many2many` (comodel `hr.job`)
- `name`: `Char`
- `resource_calendar_id`: `Many2one` (comodel `resource.calendar`)
- `start_date`: `Date`

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
title hr.leave.mandatory.day - Direct Relations
class "hr.leave.mandatory.day" as hr_leave_mandatory_day
class "hr.department" as hr_department
class "hr.job" as hr_job
class "res.company" as res_company
class "resource.calendar" as resource_calendar
hr_leave_mandatory_day --> res_company : company_id
hr_leave_mandatory_day --> resource_calendar : resource_calendar_id
hr_leave_mandatory_day .. hr_department : department_ids
hr_leave_mandatory_day .. hr_job : job_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Models]]

<!-- GENERATED:MODEL -->
