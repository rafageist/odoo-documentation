<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# PoS Preparation Display Restaurant

- Scope: Enterprise Addons
- Source: enterprise/pos_restaurant_preparation_display
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]

## Summary

Display Orders for Preparation stage.

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 1
- Views: 0
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 6

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
title PoS Preparation Display Restaurant - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n0 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n6 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_restaurant_preparation_display/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/pos_restaurant_preparation_display/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/pos_restaurant_preparation_display/Frontend|Frontend]] (6 files)

## Key models

- `pos.config`
- `pos.order`
- `pos.prep.display`
- `pos.prep.order`
- `restaurant.order.course`
- `restaurant.table`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




