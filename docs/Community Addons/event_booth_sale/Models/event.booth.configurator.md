<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.booth.configurator

- Module: [[docs/Community Addons/event_booth_sale/event_booth_sale|event_booth_sale]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/event_booth_configurator.py`
- Python classes: `EventBoothConfigurator`
- Description: Event Booth Configurator

## Field footprint

- Detected fields: 6
- Field types: `Many2many` x 2, `Many2one` x 4
- Relation fields: 6

## Sample fields

- `event_booth_category_available_ids`: `Many2many` (related `event_id.event_booth_category_available_ids`)
- `event_booth_category_id`: `Many2one` (comodel `event.booth.category`, compute `_compute_event_booth_category_id`, store `True`)
- `event_booth_ids`: `Many2many` (comodel `event.booth`, compute `_compute_event_booth_ids`, store `True`)
- `event_id`: `Many2one` (comodel `event.event`)
- `product_id`: `Many2one` (comodel `product.product`)
- `sale_order_line_id`: `Many2one` (comodel `sale.order.line`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_event_booth_category_id`, `_compute_event_booth_ids`
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
title event.booth.configurator - Direct Relations
class "event.booth.configurator" as event_booth_configurator
class "event.booth" as event_booth
class "event.booth.category" as event_booth_category
class "event.event" as event_event
class "product.product" as product_product
class "sale.order.line" as sale_order_line
event_booth_configurator --> product_product : product_id
event_booth_configurator --> sale_order_line : sale_order_line_id
event_booth_configurator --> event_event : event_id
event_booth_configurator --> event_booth_category : event_booth_category_id
event_booth_configurator .. event_booth : event_booth_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_booth_sale/Models]]

<!-- GENERATED:MODEL -->
