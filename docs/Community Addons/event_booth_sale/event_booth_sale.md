<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events Booths Sales

- Scope: Community Addons
- Source: odoo/addons/event_booth_sale
- Dependencies: [[docs/Community Addons/event_booth/event_booth|event_booth]], [[docs/Community Addons/event_sale/event_sale|event_sale]]

## Summary

Manage event booths sale

## XML Artifacts (detected)

- Views: 13
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `EventBooth`
- `EventBoothCategory`
- `event.booth.registration`
- `EventTypeBooth`
- `ProductProduct`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Events Booths Sales - Models and Relations
class AccountMove
class EventBooth
class EventBoothCategory
class "event.booth.registration" as event_booth_registration
class EventTypeBooth
class ProductProduct
class ProductTemplate
class SaleOrder
class SaleOrderLine
EventBooth --|> event_booth_registration : one2many
class "sale.order.line" as sale_order_line
EventBooth .. sale_order_line : many2many
EventBooth --> sale_order_line : many2one
class "product.product" as product_product
EventBoothCategory --> product_product : many2one
event_booth_registration --> sale_order_line : many2one
class "event.booth" as event_booth
event_booth_registration --> event_booth : many2one
class "res.partner" as res_partner
event_booth_registration --> res_partner : many2one
SaleOrder --|> event_booth : one2many
class "event.booth.category" as event_booth_category
SaleOrderLine --> event_booth_category : many2one
SaleOrderLine .. event_booth : many2many
SaleOrderLine --|> event_booth_registration : one2many
SaleOrderLine --|> event_booth : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





