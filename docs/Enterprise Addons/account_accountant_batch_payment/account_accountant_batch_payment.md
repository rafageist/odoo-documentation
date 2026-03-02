<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Batch Payment Reconciliation

- Scope: Enterprise Addons
- Source: enterprise/account_accountant_batch_payment
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]]

## Summary

Allows using Reconciliation with the Batch Payment feature.

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 5

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
title Account Batch Payment Reconciliation - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_accountant_batch_payment/Models|Models]] (3)
- Frontend: [[docs/Enterprise Addons/account_accountant_batch_payment/Frontend|Frontend]] (5 files)

## Key models

- `account.bank.statement.line`
- `account.batch.payment`
- `account.move.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




