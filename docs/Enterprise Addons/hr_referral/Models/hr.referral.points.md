<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.referral.points

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_referral_points.py`
- Python classes: `HrReferralPoints`
- Description: Points line for referrals

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Integer` x 2, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `applicant_id`: `Many2one` (comodel `hr.applicant`)
- `applicant_name`: `Char` (related `applicant_id.partner_name`)
- `company_id`: `Many2one` (comodel `res.company`)
- `hr_referral_reward_id`: `Many2one` (comodel `hr.referral.reward`)
- `points`: `Integer` (comodel `Points`)
- `ref_user_id`: `Many2one` (comodel `res.users`)
- `sequence_stage`: `Integer` (comodel `Sequence of stage`, related `stage_id.sequence`)
- `stage_id`: `Many2one` (comodel `hr.recruitment.stage`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_display_name`
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
title hr.referral.points - Direct Relations
class "hr.referral.points" as hr_referral_points
class "hr.applicant" as hr_applicant
class "hr.recruitment.stage" as hr_recruitment_stage
class "hr.referral.reward" as hr_referral_reward
class "res.company" as res_company
class "res.users" as res_users
hr_referral_points --> hr_applicant : applicant_id
hr_referral_points --> hr_referral_reward : hr_referral_reward_id
hr_referral_points --> res_users : ref_user_id
hr_referral_points --> hr_recruitment_stage : stage_id
hr_referral_points --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Models]]

<!-- GENERATED:MODEL -->
