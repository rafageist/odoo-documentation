<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sale Project - Sale Stock

- Scope: Community Addons
- Source: odoo/addons/sale_project_stock
- Dependencies: [[docs/Community Addons/sale_project/sale_project|sale_project]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/project_stock_account/project_stock_account|project_stock_account]]

## Summary

Adds a full traceability of inventory operations on the profitability report.

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 0
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title Sale Project - Sale Stock - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n0 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/sale_project_stock/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/sale_project_stock/Views|Views]] (1 files)

## Key models

- `project.project`
- `sale.order.line`
- `stock.move`
- `stock.picking`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





