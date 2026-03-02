<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.employee

- Module: [[docs/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 10
- Field types: `Char` x 1, `Many2one` x 8, `Selection` x 1
- Relation fields: 8

## Sample fields

- `exceptional_location_id`: `Many2one` (comodel `hr.work.location`, compute `_compute_exceptional_location_id`)
- `friday_location_id`: `Many2one` (comodel `hr.work.location`)
- `hr_icon_display`: `Selection`
- `monday_location_id`: `Many2one` (comodel `hr.work.location`)
- `saturday_location_id`: `Many2one` (comodel `hr.work.location`)
- `sunday_location_id`: `Many2one` (comodel `hr.work.location`)
- `thursday_location_id`: `Many2one` (comodel `hr.work.location`)
- `today_location_name`: `Char`
- `tuesday_location_id`: `Many2one` (comodel `hr.work.location`)
- `wednesday_location_id`: `Many2one` (comodel `hr.work.location`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_exceptional_location_id`, `_compute_presence_icon`, `_compute_work_location_name`, `_compute_work_location_type`
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
title hr.employee - Direct Relations
class "hr.employee" as hr_employee
class "hr.work.location" as hr_work_location
hr_employee --> hr_work_location : monday_location_id
hr_employee --> hr_work_location : tuesday_location_id
hr_employee --> hr_work_location : wednesday_location_id
hr_employee --> hr_work_location : thursday_location_id
hr_employee --> hr_work_location : friday_location_id
hr_employee --> hr_work_location : saturday_location_id
hr_employee --> hr_work_location : sunday_location_id
hr_employee --> hr_work_location : exceptional_location_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_homeworking/Models]]

<!-- GENERATED:MODEL -->
