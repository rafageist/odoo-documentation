<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Online Event Ticketing

- Version: v18
- Category: community
- Source: odoo/addons/website_event_sale
- Dependencies: [[Odoo 18/Community Addons/website_event/website_event|website_event]], [[Odoo 18/Community Addons/event_sale/event_sale|event_sale]], [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell event tickets online

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0

## Detected Models

- `Product`
- `ProductTemplate`
- `PricelistItem`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Online Event Ticketing - Models and Relations
class Product
class ProductTemplate
class PricelistItem
class SaleOrder
class SaleOrderLine
class "event.event.ticket" as event_event_ticket
Product --|> event_event_ticket : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
