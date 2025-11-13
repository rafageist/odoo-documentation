<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Events Booths Sales

- Version: v18
- Category: community
- Source: odoo/addons/event_booth_sale
- Dependencies: [[Odoo 18/Community Addons/event_booth/event_booth|event_booth]], [[Odoo 18/Community Addons/event_sale/event_sale|event_sale]]

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
- `Product`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Events Booths Sales - Models and Relations
class AccountMove
class EventBooth
class EventBoothCategory
class "event.booth.registration" as event_booth_registration
class EventTypeBooth
class Product
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
