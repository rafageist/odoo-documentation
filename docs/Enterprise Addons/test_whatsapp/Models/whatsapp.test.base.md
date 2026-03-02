<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# whatsapp.test.base

- Module: [[docs/Enterprise Addons/test_whatsapp/test_whatsapp|test_whatsapp]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/test_models.py`
- Python classes: `WhatsappTestBase`
- Description: WhatsApp Base Test
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 9
- Field types: `Char` x 2, `Datetime` x 1, `Many2many` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 5

## Sample fields

- `country_id`: `Many2one` (comodel `res.country`)
- `customer_id`: `Many2one` (comodel `res.partner`)
- `datetime`: `Datetime`
- `guest_ids`: `Many2many` (comodel `res.partner`)
- `name`: `Char` (comodel `Name`)
- `phone`: `Char` (comodel `Phone`, compute `_compute_phone`, store `True`)
- `selection_field`: `Selection`
- `selection_id`: `Many2one` (comodel `whatsapp.test.selection`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_phone`
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
title whatsapp.test.base - Direct Relations
class "whatsapp.test.base" as whatsapp_test_base
class "res.country" as res_country
class "res.partner" as res_partner
class "res.users" as res_users
class "whatsapp.test.selection" as whatsapp_test_selection
whatsapp_test_base --> res_country : country_id
whatsapp_test_base --> res_partner : customer_id
whatsapp_test_base .. res_partner : guest_ids
whatsapp_test_base --> res_users : user_id
whatsapp_test_base --> whatsapp_test_selection : selection_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/test_whatsapp/Models]]

<!-- GENERATED:MODEL -->
