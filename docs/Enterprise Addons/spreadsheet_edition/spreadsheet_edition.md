<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Spreadsheet

- Scope: Enterprise Addons
- Source: enterprise/spreadsheet_edition
- Dependencies: [[docs/Community Addons/spreadsheet/spreadsheet|spreadsheet]], [[docs/Community Addons/mail/mail|mail]], [[docs/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]]

## Summary

Spreadsheet

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 2
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 1
- Frontend asset files: 151

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
title Spreadsheet - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n2 views\n1 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n151 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/spreadsheet_edition/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/spreadsheet_edition/Views|Views]] (1 files)
- Controllers: [[docs/Enterprise Addons/spreadsheet_edition/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/spreadsheet_edition/Frontend|Frontend]] (151 files)

## Key models

- `ir.websocket`
- `spreadsheet.cell.thread`
- `spreadsheet.mixin`
- `spreadsheet.revision`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




