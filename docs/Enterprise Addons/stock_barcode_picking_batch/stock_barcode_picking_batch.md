<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Barcode for Batch Transfer

- Scope: Enterprise Addons
- Source: enterprise/stock_barcode_picking_batch
- Dependencies: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]], [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]

## Summary

Add the support of batch transfers into the barcode view

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 6
- Views: 8
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 14

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
title Barcode for Batch Transfer - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n8 views\n6 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n14 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/stock_barcode_picking_batch/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/stock_barcode_picking_batch/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/stock_barcode_picking_batch/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/stock_barcode_picking_batch/Frontend|Frontend]] (14 files)

## Key models

- `stock.move.line`
- `stock.picking`
- `stock.picking.batch`
- `stock.picking.type`
- `stock_barcode.cancel.operation`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




