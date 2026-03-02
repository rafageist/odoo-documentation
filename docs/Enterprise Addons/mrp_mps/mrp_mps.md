<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Master Production Schedule

- Scope: Enterprise Addons
- Source: enterprise/mrp_mps
- Dependencies: [[docs/Community Addons/base_import/base_import|base_import]], [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

## Summary

Master Production Schedule

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 9
- Views: 8
- Actions: 2
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 6
- Controller units: 0
- Frontend asset files: 15

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
title Master Production Schedule - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n8 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n15 files" as frontend
component "Security / Data\n1 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/mrp_mps/Models|Models]] (11)
- Views and XML: [[docs/Enterprise Addons/mrp_mps/Views|Views]] (9 files)
- Frontend: [[docs/Enterprise Addons/mrp_mps/Frontend|Frontend]] (15 files)

## Key models

- `mrp.bom`
- `mrp.mps.forecast.details`
- `mrp.mps.forecast.suggestion`
- `mrp.product.forecast`
- `mrp.production.schedule`
- `product.product`
- `product.template`
- `purchase.order`
- `res.company`
- `res.config.settings`
- `stock.rule`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




