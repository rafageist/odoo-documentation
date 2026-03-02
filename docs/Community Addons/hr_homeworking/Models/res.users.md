<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.users

- Module: [[docs/Community Addons/hr_homeworking/hr_homeworking|hr_homeworking]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_users.py`
- Python classes: `ResUsers`

## Field footprint

- Detected fields: 7
- Field types: `Many2one` x 7
- Relation fields: 7

## Sample fields

- `friday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.friday_location_id`)
- `monday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.monday_location_id`)
- `saturday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.saturday_location_id`)
- `sunday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.sunday_location_id`)
- `thursday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.thursday_location_id`)
- `tuesday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.tuesday_location_id`)
- `wednesday_location_id`: `Many2one` (comodel `hr.work.location`, related `employee_id.wednesday_location_id`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_im_status`
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
title res.users - Direct Relations
class "res.users" as res_users
class "hr.work.location" as hr_work_location
res_users --> hr_work_location : monday_location_id
res_users --> hr_work_location : tuesday_location_id
res_users --> hr_work_location : wednesday_location_id
res_users --> hr_work_location : thursday_location_id
res_users --> hr_work_location : friday_location_id
res_users --> hr_work_location : saturday_location_id
res_users --> hr_work_location : sunday_location_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_homeworking/Models]]

<!-- GENERATED:MODEL -->
