<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Online Payment

- Scope: Enterprise Addons
- Source: enterprise/account_online_payment
- Dependencies: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]], [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]]

## Summary

Initiate online payments

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 2

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
title Account Online Payment - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_online_payment/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/account_online_payment/Views|Views]] (3 files)
- Controllers: [[docs/Enterprise Addons/account_online_payment/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/account_online_payment/Frontend|Frontend]] (2 files)

## Key models

- `account.batch.payment`
- `account.online.link`
- `account.payment`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




