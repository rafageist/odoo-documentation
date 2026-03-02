<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# event.event.configurator

- Module: [[docs/Community Addons/event_sale/event_sale|event_sale]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/event_configurator.py`
- Python classes: `EventEventConfigurator`
- Description: Event Configurator

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 2, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `event_id`: `Many2one` (comodel `event.event`)
- `event_slot_id`: `Many2one` (comodel `event.slot`, compute `_compute_event_slot_id`, store `True`)
- `event_ticket_id`: `Many2one` (comodel `event.event.ticket`, compute `_compute_event_ticket_id`, store `True`)
- `has_available_tickets`: `Boolean` (comodel `Has Available Tickets`, compute `_compute_has_available_tickets`)
- `is_multi_slots`: `Boolean` (related `event_id.is_multi_slots`)
- `product_id`: `Many2one` (comodel `product.product`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_event_slot_id`, `_compute_event_ticket_id`, `_compute_has_available_tickets`
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
title event.event.configurator - Direct Relations
class "event.event.configurator" as event_event_configurator
class "event.event" as event_event
class "event.event.ticket" as event_event_ticket
class "event.slot" as event_slot
class "product.product" as product_product
event_event_configurator --> product_product : product_id
event_event_configurator --> event_event : event_id
event_event_configurator --> event_slot : event_slot_id
event_event_configurator --> event_event_ticket : event_ticket_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_sale/Models]]

<!-- GENERATED:MODEL -->
