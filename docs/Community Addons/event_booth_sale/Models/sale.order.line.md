<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order.line

- Module: [[docs/Community Addons/event_booth_sale/event_booth_sale|event_booth_sale]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/sale_order_line.py`
- Python classes: `SaleOrderLine`

## Field footprint

- Detected fields: 4
- Field types: `Many2many` x 1, `Many2one` x 1, `One2many` x 2
- Relation fields: 4

## Sample fields

- `event_booth_category_id`: `Many2one` (comodel `event.booth.category`)
- `event_booth_ids`: `One2many` (comodel `event.booth`)
- `event_booth_pending_ids`: `Many2many` (comodel `event.booth`, compute `_compute_event_booth_pending_ids`)
- `event_booth_registration_ids`: `One2many` (comodel `event.booth.registration`)

## Method hints

- Detected methods: 11
- Action methods: none
- Compute methods: `_compute_event_booth_pending_ids`, `_compute_name`
- Onchange methods: `_onchange_event_id_booth`, `_onchange_product_id_booth`

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
title sale.order.line - Direct Relations
class "sale.order.line" as sale_order_line
class "event.booth" as event_booth
class "event.booth.category" as event_booth_category
class "event.booth.registration" as event_booth_registration
sale_order_line --> event_booth_category : event_booth_category_id
sale_order_line .. event_booth : event_booth_pending_ids
sale_order_line --|> event_booth_registration : event_booth_registration_ids
sale_order_line --|> event_booth : event_booth_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_booth_sale/Models]]

<!-- GENERATED:MODEL -->
