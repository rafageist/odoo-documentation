<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.recruitment.post.job.wizard

- Module: [[docs/Enterprise Addons/hr_recruitment_integration_base/hr_recruitment_integration_base|hr_recruitment_integration_base]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_recruitment_post.py`
- Python classes: `HrRecruitmentPostJobWizard`
- Description: Post Job

## Field footprint

- Detected fields: 13
- Field types: `Char` x 1, `Date` x 4, `Html` x 1, `Json` x 1, `Many2many` x 2, `Many2one` x 3, `Selection` x 1
- Relation fields: 5

## Sample fields

- `api_data`: `Json`
- `apply_method`: `Selection`
- `campaign_end_date`: `Date`
- `campaign_start_date`: `Date`
- `company_id`: `Many2one` (comodel `res.company`)
- `date_from`: `Date` (related `job_id.date_from`)
- `date_to`: `Date` (related `job_id.date_to`)
- `industry_id`: `Many2one` (related `job_id.industry_id`)
- `job_apply_mail`: `Char` (compute `_compute_job_apply_mail`, store `True`)
- `job_id`: `Many2one` (comodel `hr.job`)
- `platform_ids`: `Many2many` (comodel `hr.recruitment.platform`)
- `post_html`: `Html` (compute `_compute_post_html`, store `True`)
- `post_ids`: `Many2many` (comodel `hr.job.post`)

## Method hints

- Detected methods: 8
- Action methods: `action_post_job`
- Compute methods: `_compute_job_apply_mail`, `_compute_post_html`
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
title hr.recruitment.post.job.wizard - Direct Relations
class "hr.recruitment.post.job.wizard" as hr_recruitment_post_job_wizard
class "hr.job" as hr_job
class "hr.job.post" as hr_job_post
class "hr.recruitment.platform" as hr_recruitment_platform
class "res.company" as res_company
hr_recruitment_post_job_wizard --> hr_job : job_id
hr_recruitment_post_job_wizard .. hr_recruitment_platform : platform_ids
hr_recruitment_post_job_wizard .. hr_job_post : post_ids
hr_recruitment_post_job_wizard --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_integration_base/Models]]

<!-- GENERATED:MODEL -->
