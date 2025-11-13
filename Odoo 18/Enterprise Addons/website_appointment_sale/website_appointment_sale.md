<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Pay to Book with eCommerce

- Version: v18
- Category: enterprise
- Source: enterprise18/website_appointment_sale
- Dependencies: [[Odoo 18/Enterprise Addons/website_appointment_account_payment/website_appointment_account_payment|website_appointment_account_payment]], [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]]

## Summary

eCommerce on appointments

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `CalendarBooking`
- `CalendarEvent`
- `ProductProduct`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Pay to Book with eCommerce - Models and Relations
class CalendarBooking
class CalendarEvent
class ProductProduct
class SaleOrder
class SaleOrderLine
class "sale.order.line" as sale_order_line
CalendarBooking --> sale_order_line : many2one
CalendarEvent --|> sale_order_line : one2many
class "calendar.booking" as calendar_booking
SaleOrderLine --|> calendar_booking : one2many
class "calendar.event" as calendar_event
SaleOrderLine --> calendar_event : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
