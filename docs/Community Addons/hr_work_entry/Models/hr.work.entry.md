<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.work.entry

- Module: [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_work_entry.py`
- Python classes: `HrWorkEntry`
- Description: HR Work Entry

## Field footprint

- Detected fields: 18
- Field types: `Boolean` x 2, `Char` x 4, `Date` x 1, `Float` x 2, `Integer` x 1, `Many2one` x 6, `Selection` x 2
- Relation fields: 6

## Sample fields

- `active`: `Boolean`
- `amount_rate`: `Float` (comodel `Pay rate`)
- `code`: `Char` (related `work_entry_type_id.code`)
- `color`: `Integer` (related `work_entry_type_id.color`)
- `company_id`: `Many2one` (comodel `res.company`)
- `conflict`: `Boolean` (comodel `Conflicts`, compute `_compute_conflict`, store `True`)
- `country_id`: `Many2one` (comodel `res.country`, related `employee_id.company_id.country_id`)
- `date`: `Date`
- `department_id`: `Many2one` (comodel `hr.department`, related `employee_id.department_id`, store `True`)
- `display_code`: `Char` (related `work_entry_type_id.display_code`)
- `duration`: `Float`
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `external_code`: `Char` (related `work_entry_type_id.external_code`)
- `name`: `Char`
- `state`: `Selection`
- `version_id`: `Many2one` (comodel `hr.version`)
- `work_entry_source`: `Selection` (related `version_id.work_entry_source`)
- `work_entry_type_id`: `Many2one` (comodel `hr.work.entry.type`)

## Method hints

- Detected methods: 20
- Action methods: `action_split`, `action_validate`
- Compute methods: `_compute_conflict`, `_compute_display_name`, `_compute_name`
- Onchange methods: `_onchange_version_id`

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
title hr.work.entry - Direct Relations
class "hr.work.entry" as hr_work_entry
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.version" as hr_version
class "hr.work.entry.type" as hr_work_entry_type
class "res.company" as res_company
class "res.country" as res_country
hr_work_entry --> hr_employee : employee_id
hr_work_entry --> hr_version : version_id
hr_work_entry --> hr_work_entry_type : work_entry_type_id
hr_work_entry --> res_company : company_id
hr_work_entry --> hr_department : department_id
hr_work_entry --> res_country : country_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_work_entry/Models]]

<!-- GENERATED:MODEL -->
