<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# CPA005 Payments

- Scope: Enterprise Addons
- Source: enterprise/l10n_ca_payment_cpa005
- Dependencies: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[docs/Community Addons/l10n_ca/l10n_ca|l10n_ca]]

## Summary

Export payments as CPA 005 AFT files

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 6
- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1
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
title CPA005 Payments - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n6 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ca_payment_cpa005/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/l10n_ca_payment_cpa005/Views|Views]] (6 files)

## Key models

- `account.batch.payment`
- `account.journal`
- `account.payment`
- `account.payment.method`
- `l10n_ca_cpa005.transaction.code`
- `res.company`
- `res.partner.bank`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




