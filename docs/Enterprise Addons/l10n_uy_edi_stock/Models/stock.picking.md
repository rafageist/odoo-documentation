<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.picking

- Module: [[docs/Enterprise Addons/l10n_uy_edi_stock/l10n_uy_edi_stock|l10n_uy_edi_stock]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPicking`
- Description: Stock Picking - Delivery Guide (Uruguay)

## Field footprint

- Detected fields: 13
- Field types: `Binary` x 1, `Boolean` x 1, `Char` x 2, `Many2many` x 2, `Many2one` x 4, `Selection` x 2, `Text` x 1
- Relation fields: 6

## Sample fields

- `l10n_latam_available_document_type_ids`: `Many2many` (comodel `l10n_latam.document.type`, compute `_compute_l10n_latam_available_document_types`)
- `l10n_latam_document_number`: `Char`
- `l10n_latam_document_type_id`: `Many2one` (comodel `l10n_latam.document.type`, compute `_compute_l10n_latam_document_type_id`, store `True`)
- `l10n_uy_edi_addenda_ids`: `Many2many` (comodel `l10n_uy_edi.addenda`)
- `l10n_uy_edi_cfe_state`: `Selection` (related `l10n_uy_edi_document_id.state`, store `True`)
- `l10n_uy_edi_cfe_uuid`: `Char` (related `l10n_uy_edi_document_id.uuid`)
- `l10n_uy_edi_document_id`: `Many2one` (comodel `l10n_uy_edi.document`)
- `l10n_uy_edi_error`: `Text` (related `l10n_uy_edi_document_id.message`)
- `l10n_uy_edi_operation_type`: `Selection` (store `True`)
- `l10n_uy_edi_pdf_report_file`: `Binary`
- `l10n_uy_edi_pdf_report_id`: `Many2one` (comodel `ir.attachment`)
- `l10n_uy_edi_reference`: `Many2one` (comodel `l10n_uy_edi.document`)
- `l10n_uy_is_cfe`: `Boolean` (compute `_compute_l10n_uy_is_cfe`)

## Method hints

- Detected methods: 26
- Action methods: `action_cancel`
- Compute methods: `_compute_display_name`, `_compute_l10n_latam_available_document_types`, `_compute_l10n_latam_document_type_id`, `_compute_l10n_uy_is_cfe`, `_compute_linked_attachment_id`
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
title stock.picking - Direct Relations
class "stock.picking" as stock_picking
class "ir.attachment" as ir_attachment
class "l10n_latam.document.type" as l10n_latam_document_type
class "l10n_uy_edi.addenda" as l10n_uy_edi_addenda
class "l10n_uy_edi.document" as l10n_uy_edi_document
stock_picking --> l10n_latam_document_type : l10n_latam_document_type_id
stock_picking .. l10n_latam_document_type : l10n_latam_available_document_type_ids
stock_picking --> l10n_uy_edi_document : l10n_uy_edi_document_id
stock_picking .. l10n_uy_edi_addenda : l10n_uy_edi_addenda_ids
stock_picking --> l10n_uy_edi_document : l10n_uy_edi_reference
stock_picking --> ir_attachment : l10n_uy_edi_pdf_report_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi_stock/Models]]

<!-- GENERATED:MODEL -->
