<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# MRP features for Quality Control

- Scope: Enterprise Addons
- Source: enterprise/quality_mrp_workorder
- Dependencies: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]], [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[docs/Community Addons/barcodes/barcodes|barcodes]]

## Summary

Quality Management with MRP

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 2
- Views: 11
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 8

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
title MRP features for Quality Control - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n11 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n8 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/quality_mrp_workorder/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/quality_mrp_workorder/Views|Views]] (2 files)
- Frontend: [[docs/Enterprise Addons/quality_mrp_workorder/Frontend|Frontend]] (8 files)

## Key models

- `mrp.production`
- `mrp.workorder`
- `product.product`
- `product.template`
- `quality.check`
- `quality.point`
- `stock.lot`
- `stock.move.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




