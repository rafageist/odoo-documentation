<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Electronic invoicing for Colombia with DIAN

- Scope: Enterprise Addons
- Source: enterprise/l10n_co_dian
- Dependencies: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Enterprise Addons/l10n_co_edi/l10n_co_edi|l10n_co_edi]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Colombian Localization for EDI documents

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 6
- Views: 11
- Actions: 2
- Menus: 0
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
title Electronic invoicing for Colombia with DIAN - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n11 views\n6 files" as views
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

- Models: [[docs/Enterprise Addons/l10n_co_dian/Models|Models]] (13)
- Views and XML: [[docs/Enterprise Addons/l10n_co_dian/Views|Views]] (6 files)

## Key models

- `account.edi.xml.ubl_dian`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.move.send`
- `certificate.certificate`
- `l10n_co_dian.claim.wizard`
- `l10n_co_dian.document`
- `l10n_co_dian.operation_mode`
- `mail.template`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




