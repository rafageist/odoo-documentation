<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# MRP Barcode

- Scope: Enterprise Addons
- Source: enterprise/stock_barcode_mrp
- Dependencies: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]], [[docs/Community Addons/mrp/mrp|mrp]]

## Summary

Process Manufacturing Orders from the barcode application

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 5
- Views: 7
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 12

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
title MRP Barcode - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n7 views\n5 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n12 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/stock_barcode_mrp/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/stock_barcode_mrp/Views|Views]] (5 files)
- Controllers: [[docs/Enterprise Addons/stock_barcode_mrp/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/stock_barcode_mrp/Frontend|Frontend]] (12 files)

## Key models

- `mrp.production`
- `mrp.production.backorder`
- `product.product`
- `stock.move`
- `stock.move.line`
- `stock.picking`
- `stock.picking.type`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




