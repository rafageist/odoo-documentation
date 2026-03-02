<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# myinvois.document

- Module: [[docs/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/myinvois_document.py`
- Python classes: `MyInvoisDocument`
- Description: MyInvois Document
- Inherits: `mail.activity.mixin`, `mail.thread`, `sequence.mixin`

## Field footprint

- Detected fields: 18
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 8, `Date` x 1, `Datetime` x 1, `Many2many` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 5

## Sample fields

- `active`: `Boolean`
- `company_currency_id`: `Many2one` (related `company_id.currency_id`)
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `invoice_ids`: `Many2many` (comodel `account.move`)
- `myinvois_custom_form_reference`: `Char`
- `myinvois_document_long_id`: `Char`
- `myinvois_error_document_hash`: `Char`
- `myinvois_exemption_reason`: `Char`
- `myinvois_external_uuid`: `Char`
- `myinvois_file`: `Binary`
- `myinvois_file_id`: `Many2one` (comodel `ir.attachment`)
- `myinvois_issuance_date`: `Date`
- `myinvois_retry_at`: `Char`
- `myinvois_state`: `Selection`
- `myinvois_submission_uid`: `Char`
- `myinvois_validation_time`: `Datetime`
- `name`: `Char` (compute `_compute_name`, store `True`)

## Method hints

- Detected methods: 38
- Action methods: `action_cancel_submission`, `action_generate_xml_file`, `action_show_myinvois_documents`, `action_submit_to_myinvois`, `action_update_submission_status`
- Compute methods: `_compute_display_name`, `_compute_linked_attachment_id`, `_compute_name`
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
title myinvois.document - Direct Relations
class "myinvois.document" as myinvois_document
class "account.move" as account_move
class "ir.attachment" as ir_attachment
class "res.company" as res_company
class "res.currency" as res_currency
myinvois_document --> res_company : company_id
myinvois_document --> res_currency : currency_id
myinvois_document --> ir_attachment : myinvois_file_id
myinvois_document .. account_move : invoice_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_my_edi/Models]]

<!-- GENERATED:MODEL -->
