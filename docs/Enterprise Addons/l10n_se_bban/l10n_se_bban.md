
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# BBAN Plusgiro Bankgiro

- Scope: Enterprise Addons
- Source: enterprise/l10n_se_bban
- Dependencies: [[docs/Enterprise Addons/account_iso20022/account_iso20022|account_iso20022]], [[docs/Community Addons/l10n_se/l10n_se|l10n_se]]

## Summary

Implements BBAN Plusgiro Bankgiro

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 2
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
title BBAN Plusgiro Bankgiro - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n2 views\n1 files" as views
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

- Models: [[docs/Enterprise Addons/l10n_se_bban/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/l10n_se_bban/Views|Views]] (1 files)

## Key models

- `account.batch.payment`
- `account.journal`
- `res.partner.bank`
- `se.bban.clear.range`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


