<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - Event

- Scope: Community Addons
- Source: odoo/addons/pos_event
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/event_product/event_product|event_product]]

## Summary

Link module between Point of Sale and Event

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `event.event`
- `event.question`
- `event.question.answer`
- `event.registration`
- `event.registration.answer`
- `event.slot`
- `event.event.ticket`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosSession`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title POS - Event - Models and Relations
class "event.event" as event_event
class "event.question" as event_question
class "event.question.answer" as event_question_answer
class "event.registration" as event_registration
class "event.registration.answer" as event_registration_answer
class "event.slot" as event_slot
class "event.event.ticket" as event_event_ticket
class PosConfig
class PosOrder
class PosOrderLine
class PosSession
class "pos.order.line" as pos_order_line
event_registration --> pos_order_line : many2one
PosOrderLine --> event_event_ticket : many2one
PosOrderLine --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





