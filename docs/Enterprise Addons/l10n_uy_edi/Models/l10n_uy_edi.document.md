<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_uy_edi.document

- Module: [[docs/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_uy_edi_document.py`
- Python classes: `L10n_Uy_EdiDocument`
- Description: Electronic Fiscal Document (CFE - UY)

## Field footprint

- Detected fields: 11
- Field types: `Binary` x 1, `Char` x 2, `Datetime` x 1, `Many2one` x 5, `Selection` x 1, `Text` x 1
- Relation fields: 5

## Sample fields

- `attachment_file`: `Binary`
- `attachment_id`: `Many2one` (comodel `ir.attachment`)
- `company_id`: `Many2one` (comodel `res.company`, compute `_compute_from_origin`)
- `l10n_latam_document_number`: `Char` (compute `_compute_from_origin`)
- `l10n_latam_document_type_id`: `Many2one` (comodel `l10n_latam.document.type`, compute `_compute_from_origin`)
- `message`: `Text`
- `move_id`: `Many2one` (comodel `account.move`)
- `partner_id`: `Many2one` (comodel `res.partner`, compute `_compute_from_origin`)
- `request_datetime`: `Datetime`
- `state`: `Selection`
- `uuid`: `Char`

## Method hints

- Detected methods: 36
- Action methods: `action_download_file`, `action_update_dgi_state`
- Compute methods: `_compute_from_origin`, `_compute_linked_attachment_id`
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
title l10n_uy_edi.document - Direct Relations
class "l10n_uy_edi.document" as l10n_uy_edi_document
class "account.move" as account_move
class "ir.attachment" as ir_attachment
class "l10n_latam.document.type" as l10n_latam_document_type
class "res.company" as res_company
class "res.partner" as res_partner
l10n_uy_edi_document --> account_move : move_id
l10n_uy_edi_document --> ir_attachment : attachment_id
l10n_uy_edi_document --> l10n_latam_document_type : l10n_latam_document_type_id
l10n_uy_edi_document --> res_company : company_id
l10n_uy_edi_document --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi/Models]]

<!-- GENERATED:MODEL -->
