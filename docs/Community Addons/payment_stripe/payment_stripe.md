<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Payment Provider: Stripe

- Scope: Community Addons
- Source: odoo/addons/payment_stripe
- Dependencies: [[docs/Community Addons/payment/payment|payment]]

## Summary

An Irish-American payment provider covering the US and many others.

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 2
- Frontend asset files: 3

## Module map

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
title Payment Provider: Stripe - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/payment_stripe/Models|Models]] (3)
- Views and XML: [[docs/Community Addons/payment_stripe/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/payment_stripe/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/payment_stripe/Frontend|Frontend]] (3 files)

## Key models

- `payment.provider`
- `payment.token`
- `payment.transaction`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






