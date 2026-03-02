<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# spreadsheet.cell.thread

- Module: [[docs/Enterprise Addons/spreadsheet_sale_management/spreadsheet_sale_management|spreadsheet_sale_management]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/spreadsheet_cell_thread.py`
- Python classes: `SpreadsheetCellThread`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `sale_order_spreadsheet_id`: `Many2one` (comodel `sale.order.spreadsheet`)

## Method hints

- Detected methods: 1
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
title spreadsheet.cell.thread - Direct Relations
class "spreadsheet.cell.thread" as spreadsheet_cell_thread
class "sale.order.spreadsheet" as sale_order_spreadsheet
spreadsheet_cell_thread --> sale_order_spreadsheet : sale_order_spreadsheet_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/spreadsheet_sale_management/Models]]

<!-- GENERATED:MODEL -->
