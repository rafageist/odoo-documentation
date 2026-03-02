<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Taiwan - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_tw_edi_ecpay
- Dependencies: [[docs/Community Addons/l10n_tw/l10n_tw|l10n_tw]]

## Summary

E-invoicing using ECpay

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 6
- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6
- Controller units: 1
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
title Taiwan - E-invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n6 views\n6 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_tw_edi_ecpay/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/l10n_tw_edi_ecpay/Views|Views]] (6 files)
- Controllers: [[docs/Community Addons/l10n_tw_edi_ecpay/Controllers|Controllers]] (1)

## Key models

- `account.move`
- `account.move.line`
- `account.move.reversal`
- `account.move.send`
- `account.tax`
- `l10n_tw_edi.invoice.cancel`
- `l10n_tw_edi.invoice.print`
- `res.company`
- `res.config.settings`
- `res.partner`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






