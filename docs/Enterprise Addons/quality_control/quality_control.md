
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Quality

- Scope: Enterprise Addons
- Source: enterprise/quality_control
- Dependencies: [[docs/Enterprise Addons/quality/quality|quality]], [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Control the quality of your products

## Generated coverage

- Models: 14
- XML files with UI/data artifacts: 8
- Views: 36
- Actions: 20
- Menus: 18
- Rules (ir.rule): 2
- Access CSV entries: 5
- Controller units: 0
- Frontend asset files: 7

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
title Quality - Generated Coverage
component "Module Overview" as overview
component "Models\n14" as models
component "Views / XML\n36 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n7 files" as frontend
component "Security / Data\n2 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/quality_control/Models|Models]] (14)
- Views and XML: [[docs/Enterprise Addons/quality_control/Views|Views]] (8 files)
- Frontend: [[docs/Enterprise Addons/quality_control/Frontend|Frontend]] (7 files)

## Key models

- `product.product`
- `product.template`
- `quality.alert`
- `quality.check`
- `quality.check.spreadsheet`
- `quality.check.wizard`
- `quality.point`
- `quality.spreadsheet.template`
- `report.quality_control.quality_worksheet`
- `report.quality_control.quality_worksheet_internal`
- `stock.lot`
- `stock.move`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


