<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Argentinean Electronic Invoicing

- Scope: Enterprise Addons
- Source: enterprise/l10n_ar_edi
- Dependencies: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]], [[docs/Community Addons/certificate/certificate|certificate]]

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 10
- Views: 11
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 3
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
title Argentinean Electronic Invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n11 views\n10 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ar_edi/Models|Models]] (10)
- Views and XML: [[docs/Enterprise Addons/l10n_ar_edi/Views|Views]] (10 files)
- Controllers: [[docs/Enterprise Addons/l10n_ar_edi/Controllers|Controllers]] (1)

## Key models

- `account.journal`
- `account.move`
- `account.move.reversal`
- `certificate.certificate`
- `l10n_ar.afipws.connection`
- `l10n_ar_afip.ws.consult`
- `product.template`
- `res.company`
- `res.config.settings`
- `res.currency`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






