<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# documents.request_wizard

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/documents_request_wizard.py`
- Python classes: `DocumentsRequest_Wizard`
- Description: Document Request

## Field footprint

- Detected fields: 11
- Field types: `Char` x 2, `Html` x 1, `Integer` x 2, `Many2many` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 5

## Sample fields

- `activity_date_deadline_range`: `Integer`
- `activity_date_deadline_range_type`: `Selection`
- `activity_note`: `Html`
- `activity_type_id`: `Many2one` (comodel `mail.activity.type`)
- `folder_id`: `Many2one` (comodel `documents.document`)
- `name`: `Char`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `requestee_id`: `Many2one` (comodel `res.partner`)
- `res_id`: `Integer` (comodel `Resource ID`)
- `res_model`: `Char` (comodel `Resource Model`)
- `tag_ids`: `Many2many` (comodel `documents.tag`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `_on_activity_type_change`

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
title documents.request_wizard - Direct Relations
class "documents.request_wizard" as documents_request_wizard
class "documents.document" as documents_document
class "documents.tag" as documents_tag
class "mail.activity.type" as mail_activity_type
class "res.partner" as res_partner
documents_request_wizard --> res_partner : requestee_id
documents_request_wizard --> res_partner : partner_id
documents_request_wizard --> mail_activity_type : activity_type_id
documents_request_wizard .. documents_tag : tag_ids
documents_request_wizard --> documents_document : folder_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Models]]

<!-- GENERATED:MODEL -->
