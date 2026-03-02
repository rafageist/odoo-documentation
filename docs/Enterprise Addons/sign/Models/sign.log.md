<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sign.log

- Module: [[docs/Enterprise Addons/sign/sign|sign]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/sign_log.py`
- Python classes: `SignLog`
- Description: Sign requests access history

## Field footprint

- Detected fields: 12
- Field types: `Char` x 3, `Datetime` x 1, `Float` x 2, `Many2one` x 4, `Selection` x 2
- Relation fields: 4

## Sample fields

- `action`: `Selection`
- `ip`: `Char` (comodel `IP address of the visitor`)
- `latitude`: `Float`
- `log_date`: `Datetime`
- `log_hash`: `Char`
- `longitude`: `Float`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `request_state`: `Selection`
- `sign_request_id`: `Many2one` (comodel `sign.request`)
- `sign_request_item_id`: `Many2one` (comodel `sign.request.item`)
- `token`: `Char`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_string_to_hash`
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
title sign.log - Direct Relations
class "sign.log" as sign_log
class "res.partner" as res_partner
class "res.users" as res_users
class "sign.request" as sign_request
class "sign.request.item" as sign_request_item
sign_log --> sign_request : sign_request_id
sign_log --> sign_request_item : sign_request_item_id
sign_log --> res_users : user_id
sign_log --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sign/Models]]

<!-- GENERATED:MODEL -->
