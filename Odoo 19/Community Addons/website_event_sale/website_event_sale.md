<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Online Event Ticketing

- Version: v19
- Category: community
- Source: odoo19/addons/website_event_sale
- Dependencies: [[Odoo 19/Community Addons/website_event/website_event|website_event]], [[Odoo 19/Community Addons/event_sale/event_sale|event_sale]], [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell event tickets online

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProductProduct`
- `ProductTemplate`
- `ProductPricelistItem`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Online Event Ticketing - Models and Relations
class ProductProduct
class ProductTemplate
class ProductPricelistItem
class SaleOrder
class SaleOrderLine
class "event.event.ticket" as event_event_ticket
ProductProduct --|> event_event_ticket : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
