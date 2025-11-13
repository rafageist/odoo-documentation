<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Events Sales

- Version: v18
- Category: community
- Source: odoo/addons/event_sale
- Dependencies: [[Odoo 18/Community Addons/event_product/event_product|event_product]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]]
## XML Artifacts (detected)

- Views: 14
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `Event`
- `EventRegistration`
- `EventTicket`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Sales - Models and Relations
class Event
class EventRegistration
class EventTicket
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "sale.order.line" as sale_order_line
Event --|> sale_order_line : one2many
class "sale.order" as sale_order
EventRegistration --> sale_order : many2one
EventRegistration --> sale_order_line : many2one
class "event.event" as event_event
SaleOrderLine --> event_event : many2one
class "event.event.ticket" as event_event_ticket
SaleOrderLine --> event_event_ticket : many2one
class "event.registration" as event_registration
SaleOrderLine --|> event_registration : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
