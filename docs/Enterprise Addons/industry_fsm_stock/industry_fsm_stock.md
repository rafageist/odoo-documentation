<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service Stock

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_stock
- Dependencies: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Validate stock moves for product added on sales orders through Field Service Management App

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 4
- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6
- Controller units: 1
- Frontend asset files: 3

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
title Field Service Stock - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n6 views\n4 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/industry_fsm_stock/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/industry_fsm_stock/Views|Views]] (4 files)
- Controllers: [[docs/Enterprise Addons/industry_fsm_stock/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/industry_fsm_stock/Frontend|Frontend]] (3 files)

## Key models

- `fsm.stock.tracking`
- `fsm.stock.tracking.line`
- `product.product`
- `project.project`
- `project.task`
- `sale.order`
- `sale.order.line`
- `stock.move`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




