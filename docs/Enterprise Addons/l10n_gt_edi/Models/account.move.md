<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/l10n_gt_edi/l10n_gt_edi|l10n_gt_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 2
- Relation fields: 4

## Sample fields

- `l10n_gt_edi_attachment_id`: `Many2one` (comodel `ir.attachment`, compute `_compute_from_l10n_gt_edi_document_ids`, store `True`)
- `l10n_gt_edi_available_doc_types`: `Char` (compute `_compute_l10n_gt_edi_available_doc_types`)
- `l10n_gt_edi_consignatory_partner`: `Many2one` (comodel `res.partner`, compute `_compute_l10n_gt_edi_consignatory_partner`, store `True`)
- `l10n_gt_edi_doc_type`: `Selection` (compute `_compute_l10n_gt_edi_doc_type`, store `True`)
- `l10n_gt_edi_document_ids`: `One2many` (comodel `l10n_gt_edi.document`)
- `l10n_gt_edi_phrase_ids`: `Many2many` (comodel `l10n_gt_edi.phrase`, compute `_compute_l10n_gt_edi_phrase_ids`, store `True`)
- `l10n_gt_edi_show_consignatory_partner`: `Boolean` (compute `_compute_l10n_gt_edi_show_consignatory_partner`)
- `l10n_gt_edi_state`: `Selection` (compute `_compute_from_l10n_gt_edi_document_ids`, store `True`)

## Method hints

- Detected methods: 22
- Action methods: none
- Compute methods: `_compute_from_l10n_gt_edi_document_ids`, `_compute_l10n_gt_edi_available_doc_types`, `_compute_l10n_gt_edi_consignatory_partner`, `_compute_l10n_gt_edi_doc_type`, `_compute_l10n_gt_edi_phrase_ids`, `_compute_l10n_gt_edi_show_consignatory_partner`, `_compute_show_reset_to_draft_button`
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
title account.move - Direct Relations
class "account.move" as account_move
class "ir.attachment" as ir_attachment
class "l10n_gt_edi.document" as l10n_gt_edi_document
class "l10n_gt_edi.phrase" as l10n_gt_edi_phrase
class "res.partner" as res_partner
account_move --|> l10n_gt_edi_document : l10n_gt_edi_document_ids
account_move .. l10n_gt_edi_phrase : l10n_gt_edi_phrase_ids
account_move --> res_partner : l10n_gt_edi_consignatory_partner
account_move --> ir_attachment : l10n_gt_edi_attachment_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_gt_edi/Models]]

<!-- GENERATED:MODEL -->
