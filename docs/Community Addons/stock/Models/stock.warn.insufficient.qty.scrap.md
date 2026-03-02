<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.warn.insufficient.qty.scrap

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_warn_insufficient_qty.py`
- Python classes: `StockWarnInsufficientQtyScrap`
- Description: Warn Insufficient Scrap Quantity
- Inherits: `stock.warn.insufficient.qty`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `scrap_id`: `Many2one` (comodel `stock.scrap`)

## Method hints

- Detected methods: 3
- Action methods: `action_cancel`, `action_done`
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
title stock.warn.insufficient.qty.scrap - Direct Relations
class "stock.warn.insufficient.qty.scrap" as stock_warn_insufficient_qty_scrap
class "stock.scrap" as stock_scrap
stock_warn_insufficient_qty_scrap --> stock_scrap : scrap_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
