<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# payment.provider

- Module: [[docs/Community Addons/website_payment/website_payment|website_payment]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/payment_provider.py`
- Python classes: `PaymentProvider`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `website_id`: `Many2one` (comodel `website`)

## Method hints

- Detected methods: 2
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
title payment.provider - Direct Relations
class "payment.provider" as payment_provider
class "website" as website
payment_provider --> website : website_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_payment/Models]]

<!-- GENERATED:MODEL -->
