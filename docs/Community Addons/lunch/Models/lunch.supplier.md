<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# lunch.supplier

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/lunch_supplier.py`
- Python classes: `LunchSupplier`
- Description: Lunch Supplier
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 42
- Field types: `Boolean` x 12, `Char` x 11, `Date` x 1, `Float` x 1, `Many2many` x 1, `Many2one` x 6, `One2many` x 3, `Selection` x 7
- Relation fields: 10

## Sample fields

- `active`: `Boolean`
- `automatic_email_time`: `Float` (comodel `Order Time`)
- `available_location_ids`: `Many2many` (comodel `lunch.location`)
- `available_today`: `Boolean` (comodel `This is True when if the supplier is available today`, compute `_compute_available_today`)
- `city`: `Char` (related `partner_id.city`)
- `company_id`: `Many2one` (comodel `res.company`, related `partner_id.company_id`, store `True`)
- `country_id`: `Many2one` (comodel `res.country`, related `partner_id.country_id`)
- `cron_id`: `Many2one` (comodel `ir.cron`)
- `delivery`: `Selection`
- `email`: `Char` (related `partner_id.email`)
- `email_formatted`: `Char` (related `partner_id.email_formatted`)
- `fri`: `Boolean`
- `moment`: `Selection`
- `mon`: `Boolean`
- `name`: `Char` (comodel `Name`, related `partner_id.name`)
- `order_deadline_passed`: `Boolean` (compute `_compute_order_deadline_passed`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `phone`: `Char` (related `partner_id.phone`)
- `recurrency_end_date`: `Date` (comodel `Until`)
- `responsible_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 15
- Action methods: `action_confirm_orders`, `action_send_orders`
- Compute methods: `_compute_available_today`, `_compute_buttons`, `_compute_display_name`, `_compute_order_deadline_passed`
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
title lunch.supplier - Direct Relations
class "lunch.supplier" as lunch_supplier
class "ir.cron" as ir_cron
class "lunch.location" as lunch_location
class "lunch.topping" as lunch_topping
class "res.company" as res_company
class "res.country" as res_country
class "res.country.state" as res_country_state
class "res.partner" as res_partner
class "res.users" as res_users
lunch_supplier --> res_partner : partner_id
lunch_supplier --> res_country_state : state_id
lunch_supplier --> res_country : country_id
lunch_supplier --> res_company : company_id
lunch_supplier --> res_users : responsible_id
lunch_supplier --> ir_cron : cron_id
lunch_supplier .. lunch_location : available_location_ids
lunch_supplier --|> lunch_topping : topping_ids_1
lunch_supplier --|> lunch_topping : topping_ids_2
lunch_supplier --|> lunch_topping : topping_ids_3
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Models]]

<!-- GENERATED:MODEL -->
