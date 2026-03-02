<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Vietnam - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_vn_edi_viettel
- Dependencies: [[docs/Community Addons/l10n_vn/l10n_vn|l10n_vn]]

## Summary

E-invoicing using SInvoice by Viettel

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 6
- Views: 7
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
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
title Vietnam - E-invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n7 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_vn_edi_viettel/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/l10n_vn_edi_viettel/Views|Views]] (6 files)

## Key models

- `account.move`
- `account.move.reversal`
- `account.move.send`
- `l10n_vn_edi_viettel.cancellation`
- `l10n_vn_edi_viettel.sinvoice.symbol`
- `l10n_vn_edi_viettel.sinvoice.template`
- `res.company`
- `res.config.settings`
- `res.partner`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






