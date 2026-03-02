<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.recruitment.stage.report

- Module: [[docs/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/hr_recruitment_stage_report.py`
- Python classes: `HrRecruitmentStageReport`
- Description: Recruitment Stage Analysis

## Field footprint

- Detected fields: 9
- Field types: `Char` x 1, `Date` x 2, `Float` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 4

## Sample fields

- `applicant_id`: `Many2one` (comodel `hr.applicant`)
- `company_id`: `Many2one` (comodel `res.company`)
- `date_begin`: `Date` (comodel `Start Date`)
- `date_end`: `Date` (comodel `End Date`)
- `days_in_stage`: `Float`
- `job_id`: `Many2one` (comodel `hr.job`)
- `name`: `Char` (comodel `Applicant Name`)
- `stage_id`: `Many2one` (comodel `hr.recruitment.stage`)
- `state`: `Selection`

## Method hints

- Detected methods: 1
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
title hr.recruitment.stage.report - Direct Relations
class "hr.recruitment.stage.report" as hr_recruitment_stage_report
class "hr.applicant" as hr_applicant
class "hr.job" as hr_job
class "hr.recruitment.stage" as hr_recruitment_stage
class "res.company" as res_company
hr_recruitment_stage_report --> hr_applicant : applicant_id
hr_recruitment_stage_report --> hr_recruitment_stage : stage_id
hr_recruitment_stage_report --> hr_job : job_id
hr_recruitment_stage_report --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_reports/Models]]

<!-- GENERATED:MODEL -->
