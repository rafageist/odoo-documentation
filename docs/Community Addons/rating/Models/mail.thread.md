<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mail.thread

- Module: [[docs/Community Addons/rating/rating|rating]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/mail_thread.py`
- Python classes: `MailThread`

## Field footprint

- Detected fields: 1
- Field types: `One2many` x 1
- Relation fields: 1

## Sample fields

- `rating_ids`: `One2many` (comodel `rating.rating`)

## Method hints

- Detected methods: 12
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
title mail.thread - Direct Relations
class "mail.thread" as mail_thread
class "rating.rating" as rating_rating
mail_thread --|> rating_rating : rating_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/rating/Models]]

<!-- GENERATED:MODEL -->
