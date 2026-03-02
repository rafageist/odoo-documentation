<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# pos.payment

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/pos_payment.py`
- Python classes: `PosPayment`
- Description: Point of Sale Payments
- Inherits: `pos.load.mixin`

## Field footprint

- Detected fields: 25
- Field types: `Boolean` x 1, `Char` x 13, `Datetime` x 1, `Float` x 1, `Many2one` x 8, `Monetary` x 1
- Relation fields: 8

## Sample fields

- `account_move_id`: `Many2one` (comodel `account.move`)
- `amount`: `Monetary`
- `card_brand`: `Char`
- `card_no`: `Char`
- `card_type`: `Char`
- `cardholder_name`: `Char`
- `company_id`: `Many2one` (comodel `res.company`, related `pos_order_id.company_id`, store `True`)
- `currency_id`: `Many2one` (comodel `res.currency`, related `pos_order_id.currency_id`)
- `currency_rate`: `Float` (related `pos_order_id.currency_rate`)
- `is_change`: `Boolean`
- `name`: `Char`
- `partner_id`: `Many2one` (comodel `res.partner`, related `pos_order_id.partner_id`)
- `payment_date`: `Datetime`
- `payment_method_authcode`: `Char`
- `payment_method_id`: `Many2one` (comodel `pos.payment.method`)
- `payment_method_issuer_bank`: `Char`
- `payment_method_payment_mode`: `Char`
- `payment_ref_no`: `Char`
- `payment_status`: `Char`
- `pos_order_id`: `Many2one` (comodel `pos.order`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_display_name`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title pos.payment - Direct Relations
class "pos.payment" as pos_payment
class "account.move" as account_move
class "pos.order" as pos_order
class "pos.payment.method" as pos_payment_method
class "pos.session" as pos_session
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.users" as res_users
pos_payment --> pos_order : pos_order_id
pos_payment --> pos_payment_method : payment_method_id
pos_payment --> res_currency : currency_id
pos_payment --> res_partner : partner_id
pos_payment --> pos_session : session_id
pos_payment --> res_users : user_id
pos_payment --> res_company : company_id
pos_payment --> account_move : account_move_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Models]]

<!-- GENERATED:MODEL -->
