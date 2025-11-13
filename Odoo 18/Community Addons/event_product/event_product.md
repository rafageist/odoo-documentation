<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Events Product

- Version: v18
- Category: community
- Source: odoo/addons/event_product
- Dependencies: [[Odoo 18/Community Addons/event/event|event]], [[Odoo 18/Community Addons/product/product|product]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Event`
- `EventTicket`
- `EventTemplateTicket`
- `Product`
- `ProductTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Product - Models and Relations
class Event
class EventTicket
class EventTemplateTicket
class Product
class ProductTemplate
class "res.currency" as res_currency
Event --> res_currency : many2one
class "product.product" as product_product
EventTemplateTicket --> product_product : many2one
class "event.event.ticket" as event_event_ticket
Product --|> event_event_ticket : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
