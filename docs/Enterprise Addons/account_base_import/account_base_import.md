<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Accounting Import

- Scope: Enterprise Addons
- Source: enterprise/account_base_import
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[docs/Community Addons/base_import/base_import|base_import]], [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]

## Summary

Improved Import in Accounting

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 8
- Views: 4
- Actions: 6
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 4

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
title Accounting Import - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n4 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_base_import/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/account_base_import/Views|Views]] (8 files)
- Frontend: [[docs/Enterprise Addons/account_base_import/Frontend|Frontend]] (4 files)

## Key models

- `account.account`
- `account.import.summary`
- `account.move.line`
- `base_import.import`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




