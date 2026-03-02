<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.recruitment.report

- Module: [[docs/Enterprise Addons/hr_recruitment_reports/hr_recruitment_reports|hr_recruitment_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/hr_recruitment_report.py`
- Python classes: `HrRecruitmentReport`
- Description: Recruitment Analysis Report

## Field footprint

- Detected fields: 19
- Field types: `Char` x 1, `Date` x 2, `Integer` x 7, `Many2one` x 8, `Selection` x 1
- Relation fields: 8

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `count`: `Integer` (comodel `Applications`)
- `create_date`: `Date` (comodel `Application Date`)
- `create_uid`: `Many2one` (comodel `res.users`)
- `date_closed`: `Date` (comodel `End Date`)
- `hired`: `Integer` (comodel `Hired`)
- `hiring_ratio`: `Integer` (comodel `Hired Ratio`)
- `in_progress`: `Integer` (comodel `In Progress`)
- `job_id`: `Many2one` (comodel `hr.job`)
- `medium_id`: `Many2one` (comodel `utm.medium`)
- `meetings_amount`: `Integer` (comodel `Meetings`)
- `name`: `Char` (comodel `Applicant Name`)
- `process_duration`: `Integer` (comodel `Process Duration`)
- `refuse_reason_id`: `Many2one` (comodel `hr.applicant.refuse.reason`)
- `refused`: `Integer` (comodel `Refused`)
- `source_id`: `Many2one` (comodel `utm.source`)
- `stage_id`: `Many2one` (comodel `hr.recruitment.stage`)
- `state`: `Selection`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 4
- Action methods: `action_open_applicant`
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
title hr.recruitment.report - Direct Relations
class "hr.recruitment.report" as hr_recruitment_report
class "hr.applicant.refuse.reason" as hr_applicant_refuse_reason
class "hr.job" as hr_job
class "hr.recruitment.stage" as hr_recruitment_stage
class "res.company" as res_company
class "res.users" as res_users
class "utm.medium" as utm_medium
class "utm.source" as utm_source
hr_recruitment_report --> res_users : user_id
hr_recruitment_report --> res_users : create_uid
hr_recruitment_report --> hr_recruitment_stage : stage_id
hr_recruitment_report --> hr_job : job_id
hr_recruitment_report --> utm_medium : medium_id
hr_recruitment_report --> utm_source : source_id
hr_recruitment_report --> hr_applicant_refuse_reason : refuse_reason_id
hr_recruitment_report --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_reports/Models]]

<!-- GENERATED:MODEL -->
