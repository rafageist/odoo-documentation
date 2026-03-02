<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.test.partner

- Module: [[docs/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mailing_models.py`
- Python classes: `MailingTestPartner`
- Description: Mailing Model with partner_id
- Inherits: `mail.thread.blacklist`

## Field footprint

- Detected fields: 3
- Field types: `Char` x 2, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `email_from`: `Char`
- `name`: `Char`
- `partner_id`: `Many2one` (comodel `res.partner`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
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
title mailing.test.partner - Direct Relations
class "mailing.test.partner" as mailing_test_partner
class "res.partner" as res_partner
mailing_test_partner --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_mass_mailing/Models]]

<!-- GENERATED:MODEL -->
