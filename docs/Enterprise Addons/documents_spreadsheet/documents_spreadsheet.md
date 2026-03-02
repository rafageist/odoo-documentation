<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents Spreadsheet

- Scope: Enterprise Addons
- Source: enterprise/documents_spreadsheet
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[docs/Community Addons/base_import/base_import|base_import]]

## Summary

Documents Spreadsheet

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 6
- Views: 10
- Actions: 3
- Menus: 2
- Rules (ir.rule): 7
- Access CSV entries: 3
- Controller units: 1
- Frontend asset files: 28

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
title Documents Spreadsheet - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n10 views\n6 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n28 files" as frontend
component "Security / Data\n7 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/documents_spreadsheet/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/documents_spreadsheet/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/documents_spreadsheet/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/documents_spreadsheet/Frontend|Frontend]] (28 files)

## Key models

- `documents.access`
- `documents.document`
- `documents.sharing`
- `ir.http`
- `save.spreadsheet.template`
- `spreadsheet.cell.thread`
- `spreadsheet.contributor`
- `spreadsheet.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




