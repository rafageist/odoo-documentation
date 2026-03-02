<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Pay to Book

- Scope: Enterprise Addons
- Source: enterprise/appointment_account_payment
- Dependencies: [[docs/Enterprise Addons/appointment/appointment|appointment]], [[docs/Community Addons/account_payment/account_payment|account_payment]]

## Summary

Up-front payment on bookings

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 3
- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4
- Controller units: 2
- Frontend asset files: 0

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
title Pay to Book - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n2 views\n3 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/appointment_account_payment/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/appointment_account_payment/Views|Views]] (3 files)
- Controllers: [[docs/Enterprise Addons/appointment_account_payment/Controllers|Controllers]] (2)

## Key models

- `account.move`
- `appointment.answer.input`
- `appointment.type`
- `calendar.booking`
- `calendar.booking.line`
- `product.product`
- `product.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




