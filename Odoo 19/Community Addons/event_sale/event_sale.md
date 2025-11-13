<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Events Sales

- Version: v19
- Category: community
- Source: odoo19/addons/event_sale
- Dependencies: [[Odoo 19/Community Addons/event_product/event_product|event_product]], [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
