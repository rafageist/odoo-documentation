<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Events Product

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/event_product
- Dependencies: [[Odoo 19/Community Addons/event/event|event]], [[Odoo 19/Community Addons/product/product|product]], [[Odoo 19/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `EventEvent`
- `EventEventTicket`
- `EventRegistration`
- `EventTypeTicket`
- `ProductProduct`
- `ProductTemplate`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Product - Models and Relations
class EventEvent
class EventEventTicket
class EventRegistration
class EventTypeTicket
class ProductProduct
class ProductTemplate
class "res.currency" as res_currency
EventEvent --> res_currency : many2one
class "product.product" as product_product
EventTypeTicket --> product_product : many2one
class "event.event.ticket" as event_event_ticket
ProductProduct --|> event_event_ticket : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


