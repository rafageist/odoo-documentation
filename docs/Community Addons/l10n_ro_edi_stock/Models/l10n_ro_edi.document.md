<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# l10n_ro_edi.document

- Module: [[docs/Community Addons/l10n_ro_edi_stock/l10n_ro_edi_stock|l10n_ro_edi_stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/l10n_ro_edi_stock_document.py`
- Python classes: `L10nRoEdiStockDocument`

## Field footprint

- Detected fields: 6
- Field types: `Char` x 3, `Many2one` x 2, `Selection` x 1
- Relation fields: 2

## Sample fields

- `invoice_id`: `Many2one`
- `l10n_ro_edi_stock_load_id`: `Char`
- `l10n_ro_edi_stock_uit`: `Char`
- `message`: `Char`
- `picking_id`: `Many2one` (comodel `stock.picking`)
- `state`: `Selection`

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
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
title l10n_ro_edi.document - Direct Relations
class "l10n_ro_edi.document" as l10n_ro_edi_document
class "stock.picking" as stock_picking
l10n_ro_edi_document --> stock_picking : picking_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ro_edi_stock/Models]]

<!-- GENERATED:MODEL -->
