<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.booth

- Module: [[docs/Community Addons/event_booth_sale/event_booth_sale|event_booth_sale]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/event_booth.py`
- Python classes: `EventBooth`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Many2many` x 1, `Many2one` x 2, `One2many` x 1
- Relation fields: 4

## Sample fields

- `event_booth_registration_ids`: `One2many` (comodel `event.booth.registration`)
- `is_paid`: `Boolean` (comodel `Is Paid`)
- `sale_order_id`: `Many2one` (related `sale_order_line_id.order_id`)
- `sale_order_line_id`: `Many2one` (comodel `sale.order.line`)
- `sale_order_line_registration_ids`: `Many2many` (comodel `sale.order.line`)

## Method hints

- Detected methods: 4
- Action methods: `action_set_paid`, `action_view_sale_order`
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
title event.booth - Direct Relations
class "event.booth" as event_booth
class "event.booth.registration" as event_booth_registration
class "sale.order.line" as sale_order_line
event_booth --|> event_booth_registration : event_booth_registration_ids
event_booth .. sale_order_line : sale_order_line_registration_ids
event_booth --> sale_order_line : sale_order_line_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_booth_sale/Models]]

<!-- GENERATED:MODEL -->
