<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Invoice Extract

- Scope: Enterprise Addons
- Source: enterprise/account_invoice_extract
- Dependencies: [[docs/Enterprise Addons/account_extract/account_extract|account_extract]]

## Summary

Extract data from invoice scans to fill them automatically

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title Account Invoice Extract - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_invoice_extract/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/account_invoice_extract/Views|Views]] (2 files)
- Controllers: [[docs/Enterprise Addons/account_invoice_extract/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/account_invoice_extract/Frontend|Frontend]] (1 files)

## Key models

- `account.move`
- `ir.attachment`
- `res.company`
- `res.config.settings`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




