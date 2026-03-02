<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.talent.pool

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_talent_pool.py`
- Python classes: `HrTalentPool`
- Description: Talent Pool
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 1, `Html` x 1, `Integer` x 2, `Many2many` x 2, `Many2one` x 2
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `categ_ids`: `Many2many` (comodel `hr.applicant.category`, store `True`)
- `color`: `Integer`
- `company_id`: `Many2one` (comodel `res.company`)
- `description`: `Html`
- `name`: `Char`
- `no_of_talents`: `Integer` (compute `_compute_talent_count`)
- `pool_manager`: `Many2one` (comodel `res.users`, store `True`)
- `talent_ids`: `Many2many` (comodel `hr.applicant`)

## Method hints

- Detected methods: 3
- Action methods: `action_talent_pool_add_talents`
- Compute methods: `_compute_talent_count`
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
title hr.talent.pool - Direct Relations
class "hr.talent.pool" as hr_talent_pool
class "hr.applicant" as hr_applicant
class "hr.applicant.category" as hr_applicant_category
class "res.company" as res_company
class "res.users" as res_users
hr_talent_pool --> res_company : company_id
hr_talent_pool --> res_users : pool_manager
hr_talent_pool .. hr_applicant : talent_ids
hr_talent_pool .. hr_applicant_category : categ_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Models]]

<!-- GENERATED:MODEL -->
