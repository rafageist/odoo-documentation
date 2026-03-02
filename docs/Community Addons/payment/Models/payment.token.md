<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.token

- Module: [[docs/Community Addons/payment/payment|payment]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/payment_token.py`
- Python classes: `PaymentToken`
- Description: Payment Token

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 1, `Char` x 3, `Many2one` x 4, `One2many` x 1, `Selection` x 1
- Relation fields: 5

## Sample fields

- `active`: `Boolean`
- `company_id`: `Many2one` (related `provider_id.company_id`, store `True`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `payment_details`: `Char`
- `payment_method_code`: `Char` (related `payment_method_id.code`)
- `payment_method_id`: `Many2one` (comodel `payment.method`)
- `provider_code`: `Selection` (related `provider_id.code`)
- `provider_id`: `Many2one` (comodel `payment.provider`)
- `provider_ref`: `Char`
- `transaction_ids`: `One2many` (comodel `payment.transaction`)

## Method hints

- Detected methods: 9
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
title payment.token - Direct Relations
class "payment.token" as payment_token
class "payment.method" as payment_method
class "payment.provider" as payment_provider
class "payment.transaction" as payment_transaction
class "res.partner" as res_partner
payment_token --> payment_provider : provider_id
payment_token --> payment_method : payment_method_id
payment_token --> res_partner : partner_id
payment_token --|> payment_transaction : transaction_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/payment/Models]]

<!-- GENERATED:MODEL -->
