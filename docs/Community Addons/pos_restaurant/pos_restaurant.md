<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Restaurant

- Scope: Community Addons
- Source: odoo/addons/pos_restaurant
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Restaurant extensions for the Point of Sale 

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 4
- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 5
- Controller units: 0
- Frontend asset files: 50

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
title Restaurant - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n8 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n50 files" as frontend
component "Security / Data\n0 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/pos_restaurant/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/pos_restaurant/Views|Views]] (4 files)
- Frontend: [[docs/Community Addons/pos_restaurant/Frontend|Frontend]] (50 files)

## Key models

- `pos.config`
- `pos.order`
- `pos.order.line`
- `pos.payment`
- `pos.preset`
- `pos.session`
- `res.config.settings`
- `restaurant.floor`
- `restaurant.order.course`
- `restaurant.table`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






