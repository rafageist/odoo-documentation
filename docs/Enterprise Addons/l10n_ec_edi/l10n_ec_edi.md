<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Ecuadorian Accounting EDI

- Scope: Enterprise Addons
- Source: enterprise/l10n_ec_edi
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/certificate/certificate|certificate]], [[docs/Community Addons/l10n_ec/l10n_ec|l10n_ec]]

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 13
- Views: 15
- Actions: 3
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 6
- Controller units: 1
- Frontend asset files: 1

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
title Ecuadorian Accounting EDI - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n15 views\n13 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n2 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ec_edi/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/l10n_ec_edi/Views|Views]] (13 files)
- Controllers: [[docs/Enterprise Addons/l10n_ec_edi/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/l10n_ec_edi/Frontend|Frontend]] (1 files)

## Key models

- `account.chart.template`
- `account.edi.format`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.move.send`
- `account.tax`
- `certificate.certificate`
- `l10n_ec.reimbursement`
- `l10n_ec.taxpayer.type`
- `l10n_ec.wizard.account.withhold`
- `l10n_ec.wizard.account.withhold.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





