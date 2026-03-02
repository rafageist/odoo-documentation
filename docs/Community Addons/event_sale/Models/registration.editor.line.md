<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# registration.editor.line

- Module: [[docs/Community Addons/event_sale/event_sale|event_sale]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/event_edit_registration.py`
- Python classes: `RegistrationEditorLine`
- Description: Edit Attendee Line on Sales Confirmation

## Field footprint

- Detected fields: 10
- Field types: `Char` x 3, `Many2one` x 7
- Relation fields: 7

## Sample fields

- `company_id`: `Many2one` (related `event_id.company_id`)
- `editor_id`: `Many2one` (comodel `registration.editor`)
- `email`: `Char`
- `event_id`: `Many2one` (comodel `event.event`)
- `event_slot_id`: `Many2one` (comodel `event.slot`)
- `event_ticket_id`: `Many2one` (comodel `event.event.ticket`)
- `name`: `Char`
- `phone`: `Char`
- `registration_id`: `Many2one` (comodel `event.registration`)
- `sale_order_line_id`: `Many2one` (comodel `sale.order.line`)

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
title registration.editor.line - Direct Relations
class "registration.editor.line" as registration_editor_line
class "event.event" as event_event
class "event.event.ticket" as event_event_ticket
class "event.registration" as event_registration
class "event.slot" as event_slot
class "registration.editor" as registration_editor
class "sale.order.line" as sale_order_line
registration_editor_line --> registration_editor : editor_id
registration_editor_line --> sale_order_line : sale_order_line_id
registration_editor_line --> event_event : event_id
registration_editor_line --> event_registration : registration_id
registration_editor_line --> event_slot : event_slot_id
registration_editor_line --> event_event_ticket : event_ticket_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/event_sale/Models]]

<!-- GENERATED:MODEL -->
