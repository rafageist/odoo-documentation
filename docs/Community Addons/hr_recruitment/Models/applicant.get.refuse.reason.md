<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# applicant.get.refuse.reason

- Module: [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/applicant_refuse_reason.py`
- Python classes: `ApplicantGetRefuseReason`
- Description: Get Refuse Reason
- Inherits: `mail.composer.mixin`

## Field footprint

- Detected fields: 11
- Field types: `Binary` x 1, `Boolean` x 2, `Char` x 1, `Integer` x 1, `Many2many` x 3, `Many2one` x 2, `Text` x 1
- Relation fields: 5

## Sample fields

- `applicant_ids`: `Many2many` (comodel `hr.applicant`)
- `applicant_without_email`: `Text` (compute `_compute_applicant_without_email`)
- `attachment_ids`: `Many2many` (comodel `ir.attachment`, compute `_compute_from_template_id`, store `True`)
- `duplicate_applicant_ids`: `Many2many` (comodel `hr.applicant`, compute `_compute_duplicate_applicant_ids`, store `True`)
- `duplicate_applicant_ids_domain`: `Binary` (compute `_compute_duplicate_applicant_ids_domain`)
- `duplicates`: `Boolean`
- `duplicates_count`: `Integer` (comodel `Duplicates Count`, compute `_compute_duplicate_applicant_ids_domain`)
- `refuse_reason_id`: `Many2one` (comodel `hr.applicant.refuse.reason`)
- `scheduled_date`: `Char` (comodel `Scheduled Date`, compute `_compute_from_template_id`, store `True`)
- `send_mail`: `Boolean` (comodel `Send Email`)
- `template_id`: `Many2one` (comodel `mail.template`, compute `_compute_template_id`, store `True`)

## Method hints

- Detected methods: 11
- Action methods: `action_refuse_reason_apply`
- Compute methods: `_compute_applicant_without_email`, `_compute_duplicate_applicant_ids`, `_compute_duplicate_applicant_ids_domain`, `_compute_from_template_id`, `_compute_render_model`, `_compute_template_id`
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
title applicant.get.refuse.reason - Direct Relations
class "applicant.get.refuse.reason" as applicant_get_refuse_reason
class "hr.applicant" as hr_applicant
class "hr.applicant.refuse.reason" as hr_applicant_refuse_reason
class "ir.attachment" as ir_attachment
class "mail.template" as mail_template
applicant_get_refuse_reason --> hr_applicant_refuse_reason : refuse_reason_id
applicant_get_refuse_reason .. hr_applicant : applicant_ids
applicant_get_refuse_reason --> mail_template : template_id
applicant_get_refuse_reason .. hr_applicant : duplicate_applicant_ids
applicant_get_refuse_reason .. ir_attachment : attachment_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment/Models]]

<!-- GENERATED:MODEL -->
