<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Third Party and Deferred/Electronic Checks Management

- Scope: Community Addons
- Source: odoo/addons/l10n_latam_check
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/base_vat/base_vat|base_vat]]

## Summary

Checks Management

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 5
- Views: 11
- Actions: 3
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4
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
title Third Party and Deferred/Electronic Checks Management - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n11 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_latam_check/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/l10n_latam_check/Views|Views]] (5 files)

## Key models

- `account.chart.template`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.payment`
- `account.payment.method`
- `account.payment.register`
- `l10n_latam.check`
- `l10n_latam.payment.mass.transfer`
- `l10n_latam.payment.register.check`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






