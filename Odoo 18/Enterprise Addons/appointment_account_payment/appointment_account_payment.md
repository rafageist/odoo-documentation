<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Pay to Book

- Version: v18
- Category: enterprise
- Source: enterprise18/appointment_account_payment
- Dependencies: [[Odoo 18/Enterprise Addons/appointment/appointment|appointment]], [[Odoo 18/Community Addons/account_payment/account_payment|account_payment]]

## Summary

Up-front payment on bookings

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `AppointmentAnswerInput`
- `AppointmentType`
- `calendar.booking`
- `calendar.booking.line`
- `ProductProduct`
- `ProductTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Pay to Book - Models and Relations
class AccountMove
class AppointmentAnswerInput
class AppointmentType
class "calendar.booking" as calendar_booking
class "calendar.booking.line" as calendar_booking_line
class ProductProduct
class ProductTemplate
AccountMove --|> calendar_booking : one2many
AppointmentAnswerInput --> calendar_booking : many2one
class "product.product" as product_product
AppointmentType --> product_product : many2one
class "appointment.answer.input" as appointment_answer_input
calendar_booking --|> appointment_answer_input : one2many
class "appointment.invite" as appointment_invite
calendar_booking --> appointment_invite : many2one
class "appointment.type" as appointment_type
calendar_booking --> appointment_type : many2one
class "res.partner" as res_partner
calendar_booking .. res_partner : many2many
calendar_booking --> res_partner : many2one
calendar_booking --|> calendar_booking_line : one2many
class "res.users" as res_users
calendar_booking --> res_users : many2one
class "account.move" as account_move
calendar_booking --> account_move : many2one
calendar_booking --> product_product : many2one
class "calendar.event" as calendar_event
calendar_booking --> calendar_event : many2one
class "appointment.resource" as appointment_resource
calendar_booking_line --> appointment_resource : many2one
calendar_booking_line --> calendar_booking : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
