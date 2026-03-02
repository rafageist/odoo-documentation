<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.applicant

- Module: [[docs/Community Addons/hr_recruitment_skills/hr_recruitment_skills|hr_recruitment_skills]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_applicant.py`
- Python classes: `HrApplicant`

## Field footprint

- Detected fields: 6
- Field types: `Integer` x 1, `Many2many` x 3, `One2many` x 2
- Relation fields: 5

## Sample fields

- `applicant_skill_ids`: `One2many` (comodel `hr.applicant.skill`)
- `current_applicant_skill_ids`: `One2many` (comodel `hr.applicant.skill`, compute `_compute_current_applicant_skill_ids`)
- `matching_score`: `Integer` (compute `_compute_matching_skill_ids`)
- `matching_skill_ids`: `Many2many` (comodel `hr.skill`, compute `_compute_matching_skill_ids`)
- `missing_skill_ids`: `Many2many` (comodel `hr.skill`, compute `_compute_matching_skill_ids`)
- `skill_ids`: `Many2many` (comodel `hr.skill`, compute `_compute_skill_ids`, store `True`)

## Method hints

- Detected methods: 8
- Action methods: `action_add_to_job`
- Compute methods: `_compute_current_applicant_skill_ids`, `_compute_matching_skill_ids`, `_compute_skill_ids`
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
title hr.applicant - Direct Relations
class "hr.applicant" as hr_applicant
class "hr.applicant.skill" as hr_applicant_skill
class "hr.skill" as hr_skill
hr_applicant --|> hr_applicant_skill : applicant_skill_ids
hr_applicant --|> hr_applicant_skill : current_applicant_skill_ids
hr_applicant .. hr_skill : skill_ids
hr_applicant .. hr_skill : matching_skill_ids
hr_applicant .. hr_skill : missing_skill_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_skills/Models]]

<!-- GENERATED:MODEL -->
