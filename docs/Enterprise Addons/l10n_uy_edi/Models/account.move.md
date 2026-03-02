<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 1, `Many2many` x 1, `Many2one` x 2, `Selection` x 4, `Text` x 1
- Relation fields: 3

## Sample fields

- `l10n_uy_edi_addenda_ids`: `Many2many` (comodel `l10n_uy_edi.addenda`)
- `l10n_uy_edi_cfe_sale_mode`: `Selection`
- `l10n_uy_edi_cfe_state`: `Selection` (related `l10n_uy_edi_document_id.state`, store `True`)
- `l10n_uy_edi_cfe_transport_route`: `Selection`
- `l10n_uy_edi_cfe_uuid`: `Char` (related `l10n_uy_edi_document_id.uuid`)
- `l10n_uy_edi_document_id`: `Many2one` (comodel `l10n_uy_edi.document`)
- `l10n_uy_edi_error`: `Text` (related `l10n_uy_edi_document_id.message`)
- `l10n_uy_edi_is_needed`: `Boolean` (compute `_compute_l10n_uy_edi_is_needed`)
- `l10n_uy_edi_journal_type`: `Selection` (related `journal_id.l10n_uy_edi_type`)
- `l10n_uy_edi_xml_attachment_id`: `Many2one` (comodel `ir.attachment`, compute `_compute_l10n_uy_edi_xml_attachment_id`)

## Method hints

- Detected methods: 44
- Action methods: `action_post`
- Compute methods: `_compute_l10n_latam_document_type`, `_compute_l10n_uy_edi_is_needed`, `_compute_l10n_uy_edi_xml_attachment_id`, `_compute_name`, `_compute_show_reset_to_draft_button`
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
class "l10n_uy_edi.addenda" as l10n_uy_edi_addenda
class "l10n_uy_edi.document" as l10n_uy_edi_document
account_move --> l10n_uy_edi_document : l10n_uy_edi_document_id
account_move .. l10n_uy_edi_addenda : l10n_uy_edi_addenda_ids
account_move --> ir_attachment : l10n_uy_edi_xml_attachment_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi/Models]]

<!-- GENERATED:MODEL -->
