<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# pos.order

- Module: [[docs/Enterprise Addons/l10n_mx_edi_pos/l10n_mx_edi_pos|l10n_mx_edi_pos]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/pos_order.py`
- Python classes: `PosOrder`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 3, `Char` x 1, `Many2many` x 1, `Many2one` x 2, `Selection` x 3
- Relation fields: 3

## Sample fields

- `l10n_mx_edi_cfdi_attachment_id`: `Many2one` (comodel `ir.attachment`, compute `_compute_l10n_mx_edi_cfdi_state_and_attachment`, store `True`)
- `l10n_mx_edi_cfdi_sat_state`: `Selection` (compute `_compute_l10n_mx_edi_cfdi_state_and_attachment`, store `True`)
- `l10n_mx_edi_cfdi_state`: `Selection` (compute `_compute_l10n_mx_edi_cfdi_state_and_attachment`, store `True`)
- `l10n_mx_edi_cfdi_to_public`: `Boolean` (compute `_compute_l10n_mx_edi_cfdi_to_public`, store `True`)
- `l10n_mx_edi_cfdi_uuid`: `Char` (compute `_compute_l10n_mx_edi_cfdi_uuid`, store `True`)
- `l10n_mx_edi_document_ids`: `Many2many` (comodel `l10n_mx_edi.document`)
- `l10n_mx_edi_is_cfdi_needed`: `Boolean` (compute `_compute_l10n_mx_edi_is_cfdi_needed`, store `True`)
- `l10n_mx_edi_payment_method_id`: `Many2one` (comodel `l10n_mx_edi.payment.method`, compute `_compute_l10n_mx_edi_payment_method_id`)
- `l10n_mx_edi_update_sat_needed`: `Boolean` (compute `_compute_l10n_mx_edi_update_sat_needed`)
- `l10n_mx_edi_usage`: `Selection`

## Method hints

- Detected methods: 34
- Action methods: `action_pos_order_invoice`
- Compute methods: `_compute_l10n_mx_edi_cfdi_state_and_attachment`, `_compute_l10n_mx_edi_cfdi_to_public`, `_compute_l10n_mx_edi_cfdi_uuid`, `_compute_l10n_mx_edi_is_cfdi_needed`, `_compute_l10n_mx_edi_payment_method_id`, `_compute_l10n_mx_edi_update_sat_needed`
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
title pos.order - Direct Relations
class "pos.order" as pos_order
class "ir.attachment" as ir_attachment
class "l10n_mx_edi.document" as l10n_mx_edi_document
class "l10n_mx_edi.payment.method" as l10n_mx_edi_payment_method
pos_order .. l10n_mx_edi_document : l10n_mx_edi_document_ids
pos_order --> ir_attachment : l10n_mx_edi_cfdi_attachment_id
pos_order --> l10n_mx_edi_payment_method : l10n_mx_edi_payment_method_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_pos/Models]]

<!-- GENERATED:MODEL -->
