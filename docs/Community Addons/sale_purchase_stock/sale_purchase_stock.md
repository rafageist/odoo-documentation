<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# MTO Sale <-> Purchase

- Scope: Community Addons
- Source: odoo/addons/sale_purchase_stock
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[docs/Community Addons/sale_purchase/sale_purchase|sale_purchase]]

## Summary

SO/PO relation in case of MTO

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
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
title MTO Sale <-> Purchase - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n1 views\n1 files" as views
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

- Models: [[docs/Community Addons/sale_purchase_stock/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/sale_purchase_stock/Views|Views]] (1 files)

## Key models

- `purchase.order`
- `purchase.order.line`
- `sale.order`
- `stock.move`
- `stock.rule`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





