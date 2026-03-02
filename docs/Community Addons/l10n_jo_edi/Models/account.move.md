<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.move

- Module: [[docs/Community Addons/l10n_jo_edi/l10n_jo_edi|l10n_jo_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/account_move.py`
- Python classes: `AccountMove`

## Field footprint

- Detected fields: 10
- Field types: `Binary` x 2, `Boolean` x 1, `Char` x 2, `Many2one` x 2, `Selection` x 2, `Text` x 1
- Relation fields: 2

## Sample fields

- `l10n_jo_edi_computed_xml`: `Binary` (compute `_compute_l10n_jo_edi_computed_xml`)
- `l10n_jo_edi_error`: `Text`
- `l10n_jo_edi_invoice_type`: `Selection` (compute `_compute_l10n_jo_edi_invoice_type`, store `True`)
- `l10n_jo_edi_is_needed`: `Boolean` (compute `_compute_l10n_jo_edi_is_needed`)
- `l10n_jo_edi_qr`: `Char`
- `l10n_jo_edi_state`: `Selection`
- `l10n_jo_edi_uuid`: `Char` (compute `_compute_l10n_jo_edi_uuid`, store `True`)
- `l10n_jo_edi_xml_attachment_file`: `Binary`
- `l10n_jo_edi_xml_attachment_id`: `Many2one` (comodel `ir.attachment`)
- `reversed_entry_id`: `Many2one`

## Method hints

- Detected methods: 24
- Action methods: none
- Compute methods: `_compute_l10n_jo_edi_computed_xml`, `_compute_l10n_jo_edi_invoice_type`, `_compute_l10n_jo_edi_is_needed`, `_compute_l10n_jo_edi_uuid`, `_compute_preferred_payment_method_line_id`, `_compute_show_reset_to_draft_button`
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
account_move --> ir_attachment : l10n_jo_edi_xml_attachment_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_jo_edi/Models]]

<!-- GENERATED:MODEL -->
