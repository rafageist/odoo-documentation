<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Repairs

- Scope: Community Addons
- Source: odoo/addons/repair
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Repair damaged products

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 10
- Views: 18
- Actions: 9
- Menus: 8
- Rules (ir.rule): 1
- Access CSV entries: 3
- Controller units: 0
- Frontend asset files: 2

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
title Repairs - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n18 views\n10 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n1 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/repair/Models|Models]] (15)
- Views and XML: [[docs/Community Addons/repair/Views|Views]] (10 files)
- Frontend: [[docs/Community Addons/repair/Frontend|Frontend]] (2 files)

## Key models

- `product.product`
- `product.template`
- `repair.order`
- `repair.tags`
- `sale.order`
- `sale.order.line`
- `stock.forecasted_product_product`
- `stock.lot`
- `stock.move`
- `stock.move.line`
- `stock.picking`
- `stock.picking.type`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






