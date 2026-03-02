
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sale order spreadsheet

- Scope: Enterprise Addons
- Source: enterprise/spreadsheet_sale_management
- Dependencies: [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 4
- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 8
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 11

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
title Sale order spreadsheet - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n4 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n8 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/spreadsheet_sale_management/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/spreadsheet_sale_management/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/spreadsheet_sale_management/Frontend|Frontend]] (11 files)

## Key models

- `sale.order`
- `sale.order.spreadsheet`
- `sale.order.template`
- `spreadsheet.cell.thread`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


