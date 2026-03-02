<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.referral.report

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/hr_referral_report.py`
- Python classes: `HrReferralReport`
- Description: Employee Referral Report

## Field footprint

- Detected fields: 12
- Field types: `Date` x 1, `Integer` x 4, `Many2one` x 6, `Selection` x 1
- Relation fields: 6

## Sample fields

- `applicant_id`: `Many2one` (comodel `hr.applicant`)
- `company_id`: `Many2one` (comodel `res.company`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `earned_points`: `Integer` (comodel `Earned Points`)
- `employee_referral_hired`: `Integer` (comodel `Employee Referral Hired`)
- `employee_referral_refused`: `Integer` (comodel `Employee Referral Refused`)
- `job_id`: `Many2one` (comodel `hr.job`)
- `medium_id`: `Many2one` (comodel `utm.medium`)
- `points_not_hired`: `Integer` (comodel `Points Given For Not Hired`)
- `ref_user_id`: `Many2one` (comodel `res.users`)
- `referral_state`: `Selection`
- `write_date`: `Date`

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
title hr.referral.report - Direct Relations
class "hr.referral.report" as hr_referral_report
class "hr.applicant" as hr_applicant
class "hr.department" as hr_department
class "hr.job" as hr_job
class "res.company" as res_company
class "res.users" as res_users
class "utm.medium" as utm_medium
hr_referral_report --> hr_applicant : applicant_id
hr_referral_report --> res_users : ref_user_id
hr_referral_report --> hr_job : job_id
hr_referral_report --> hr_department : department_id
hr_referral_report --> utm_medium : medium_id
hr_referral_report --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Models]]

<!-- GENERATED:MODEL -->
