<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# LATAM Document

- Scope: Community Addons
- Source: odoo/addons/l10n_latam_invoice_document
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_debit_note/account_debit_note|account_debit_note]]

## Summary

LATAM Document Types

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 6
- Views: 10
- Actions: 1
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
title LATAM Document - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n10 views\n6 files" as views
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

- Models: [[docs/Community Addons/l10n_latam_invoice_document/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/l10n_latam_invoice_document/Views|Views]] (6 files)

## Key models

- `account.chart.template`
- `account.debit.note`
- `account.invoice.report`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.move.reversal`
- `l10n_latam.document.type`
- `res.company`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






