<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.job

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_job.py`
- Python classes: `HrJob`
- Description: Job Position
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 1, `Char` x 1, `Html` x 1, `Integer` x 4, `Many2many` x 1, `Many2one` x 4, `One2many` x 1, `Text` x 1
- Relation fields: 6

## Sample fields

- `active`: `Boolean`
- `allowed_user_ids`: `Many2many` (comodel `res.users`, compute `_compute_allowed_user_ids`)
- `company_id`: `Many2one` (comodel `res.company`)
- `contract_type_id`: `Many2one` (comodel `hr.contract.type`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `description`: `Html`
- `employee_ids`: `One2many` (comodel `hr.employee`)
- `expected_employees`: `Integer` (compute `_compute_employees`)
- `name`: `Char`
- `no_of_employee`: `Integer` (compute `_compute_employees`)
- `no_of_recruitment`: `Integer`
- `requirements`: `Text` (comodel `Requirements`)
- `sequence`: `Integer`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_allowed_user_ids`, `_compute_employees`
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
title hr.job - Direct Relations
class "hr.job" as hr_job
class "hr.contract.type" as hr_contract_type
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "res.company" as res_company
class "res.users" as res_users
hr_job --|> hr_employee : employee_ids
hr_job --> res_users : user_id
hr_job .. res_users : allowed_user_ids
hr_job --> hr_department : department_id
hr_job --> res_company : company_id
hr_job --> hr_contract_type : contract_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr/Models]]

<!-- GENERATED:MODEL -->
