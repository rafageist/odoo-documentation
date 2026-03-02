<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# appraisal.ask.feedback

- Module: [[docs/Enterprise Addons/hr_appraisal_survey/hr_appraisal_survey|hr_appraisal_survey]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/appraisal_ask_feedback.py`
- Python classes: `AppraisalAskFeedback`
- Description: Ask Feedback for Appraisal
- Inherits: `hr.mixin`, `mail.composer.mixin`

## Field footprint

- Detected fields: 10
- Field types: `Date` x 1, `Html` x 1, `Many2many` x 3, `Many2one` x 5
- Relation fields: 8

## Sample fields

- `allowed_survey_template_ids`: `Many2many` (comodel `survey.survey`, compute `_compute_allowed_survey_template_ids`)
- `appraisal_id`: `Many2one` (comodel `hr.appraisal`)
- `attachment_ids`: `Many2many` (comodel `ir.attachment`)
- `author_id`: `Many2one` (comodel `res.partner`)
- `deadline`: `Date` (compute `_compute_deadline`, store `True`)
- `employee_id`: `Many2one` (related `appraisal_id.employee_id`)
- `employee_ids`: `Many2many` (comodel `hr.employee`)
- `survey_template_id`: `Many2one` (comodel `survey.survey`, compute `_compute_survey_template_id`, store `True`)
- `template_id`: `Many2one`
- `user_body`: `Html` (comodel `User Contents`)

## Method hints

- Detected methods: 13
- Action methods: `action_save_as_template`, `action_send`
- Compute methods: `_compute_allowed_survey_template_ids`, `_compute_body`, `_compute_deadline`, `_compute_render_model`, `_compute_subject`, `_compute_survey_template_id`
- Onchange methods: `_onchange_employee_ids`, `_onchange_template_id`

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
title appraisal.ask.feedback - Direct Relations
class "appraisal.ask.feedback" as appraisal_ask_feedback
class "hr.appraisal" as hr_appraisal
class "hr.employee" as hr_employee
class "ir.attachment" as ir_attachment
class "res.partner" as res_partner
class "survey.survey" as survey_survey
appraisal_ask_feedback --> hr_appraisal : appraisal_id
appraisal_ask_feedback .. ir_attachment : attachment_ids
appraisal_ask_feedback --> res_partner : author_id
appraisal_ask_feedback .. survey_survey : allowed_survey_template_ids
appraisal_ask_feedback --> survey_survey : survey_template_id
appraisal_ask_feedback .. hr_employee : employee_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_survey/Models]]

<!-- GENERATED:MODEL -->
