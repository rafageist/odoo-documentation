<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.employee.public

- Module: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_employee_public.py`
- Python classes: `HrEmployeePublic`

## Field footprint

- Detected fields: 4
- Field types: `One2many` x 4
- Relation fields: 4

## Sample fields

- `certification_ids`: `One2many` (comodel `hr.employee.skill`, related `employee_id.certification_ids`)
- `current_employee_skill_ids`: `One2many` (comodel `hr.employee.skill`, related `employee_id.current_employee_skill_ids`)
- `employee_skill_ids`: `One2many` (comodel `hr.employee.skill`)
- `resume_line_ids`: `One2many` (comodel `hr.resume.line`)

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
class "hr.employee.skill" as hr_employee_skill
class "hr.resume.line" as hr_resume_line
hr_employee_public --|> hr_resume_line : resume_line_ids
hr_employee_public --|> hr_employee_skill : employee_skill_ids
hr_employee_public --|> hr_employee_skill : current_employee_skill_ids
hr_employee_public --|> hr_employee_skill : certification_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_skills/Models]]

<!-- GENERATED:MODEL -->
