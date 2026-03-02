<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.employee.public

- Module: [[docs/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_employee_public.py`
- Python classes: `HrEmployeePublic`

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Many2one` x 7
- Relation fields: 7

## Sample fields

- `friday_location_id`: `Many2one` (comodel `hr.work.location`)
- `monday_location_id`: `Many2one` (comodel `hr.work.location`)
- `saturday_location_id`: `Many2one` (comodel `hr.work.location`)
- `sunday_location_id`: `Many2one` (comodel `hr.work.location`)
- `thursday_location_id`: `Many2one` (comodel `hr.work.location`)
- `today_location_name`: `Char`
- `tuesday_location_id`: `Many2one` (comodel `hr.work.location`)
- `wednesday_location_id`: `Many2one` (comodel `hr.work.location`)

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
title hr.employee.public - Direct Relations
class "hr.employee.public" as hr_employee_public
class "hr.work.location" as hr_work_location
hr_employee_public --> hr_work_location : monday_location_id
hr_employee_public --> hr_work_location : tuesday_location_id
hr_employee_public --> hr_work_location : wednesday_location_id
hr_employee_public --> hr_work_location : thursday_location_id
hr_employee_public --> hr_work_location : friday_location_id
hr_employee_public --> hr_work_location : saturday_location_id
hr_employee_public --> hr_work_location : sunday_location_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_homeworking/Models]]

<!-- GENERATED:MODEL -->
