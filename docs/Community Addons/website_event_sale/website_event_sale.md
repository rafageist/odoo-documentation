
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Online Event Ticketing

- Scope: Community Addons
- Source: odoo/addons/website_event_sale
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Community Addons/event_sale/event_sale|event_sale]], [[docs/Community Addons/website_sale/website_sale|website_sale]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

