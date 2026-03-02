<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events Sales

- Scope: Community Addons
- Source: odoo/addons/event_sale
- Dependencies: [[docs/Community Addons/event_product/event_product|event_product]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## XML Artifacts (detected)

- Views: 12
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `EventEvent`
- `EventRegistration`
- `EventEventTicket`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Events Sales - Models and Relations
class EventEvent
class EventRegistration
class EventEventTicket
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "sale.order.line" as sale_order_line
EventEvent --|> sale_order_line : one2many
class "sale.order" as sale_order
EventRegistration --> sale_order : many2one
EventRegistration --> sale_order_line : many2one
class "event.event" as event_event
SaleOrderLine --> event_event : many2one
class "event.slot" as event_slot
SaleOrderLine --> event_slot : many2one
class "event.event.ticket" as event_event_ticket
SaleOrderLine --> event_event_ticket : many2one
class "event.registration" as event_registration
SaleOrderLine --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





