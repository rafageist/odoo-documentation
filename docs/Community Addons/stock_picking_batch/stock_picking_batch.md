<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Warehouse Management: Batch Transfer

- Scope: Community Addons
- Source: odoo/addons/stock_picking_batch
- Dependencies: [[docs/Community Addons/stock/stock|stock]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 9
- Views: 22
- Actions: 9
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 3
- Controller units: 0
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
title Warehouse Management: Batch Transfer - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n22 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n1 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/stock_picking_batch/Models|Models]] (8)
- Views and XML: [[docs/Community Addons/stock_picking_batch/Views|Views]] (9 files)
- Frontend: [[docs/Community Addons/stock_picking_batch/Frontend|Frontend]] (1 files)

## Key models

- `stock.add.to.wave`
- `stock.move`
- `stock.move.line`
- `stock.picking`
- `stock.picking.batch`
- `stock.picking.to.batch`
- `stock.picking.type`
- `stock.warehouse`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





