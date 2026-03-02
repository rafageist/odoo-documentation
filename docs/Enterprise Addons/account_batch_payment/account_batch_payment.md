
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Batch Payment

- Scope: Enterprise Addons
- Source: enterprise/account_batch_payment
- Dependencies: [[docs/Community Addons/account/account|account]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 7
- Views: 12
- Actions: 4
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 5
- Controller units: 0
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
title Batch Payment - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n12 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_batch_payment/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/account_batch_payment/Views|Views]] (7 files)

## Key models

- `account.batch.error.wizard`
- `account.batch.error.wizard.line`
- `account.batch.payment`
- `account.create.batch.error.wizard`
- `account.journal`
- `account.payment`
- `account.payment.method`
- `report.account_batch_payment.print_batch_payment`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



