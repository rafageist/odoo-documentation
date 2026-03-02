<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# UK BACS Payment Files

- Scope: Enterprise Addons
- Source: enterprise/l10n_uk_bacs
- Dependencies: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/l10n_uk/l10n_uk|l10n_uk]]

## Summary

Export payments as BACS Direct Debit and Direct Credit files

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 5
- Views: 7
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2
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
title UK BACS Payment Files - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n7 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_uk_bacs/Models|Models]] (9)
- Views and XML: [[docs/Enterprise Addons/l10n_uk_bacs/Views|Views]] (5 files)

## Key models

- `account.batch.payment`
- `account.journal`
- `account.move`
- `account.payment`
- `account.payment.method`
- `bacs.ddi`
- `res.company`
- `res.config.settings`
- `res.partner.bank`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




