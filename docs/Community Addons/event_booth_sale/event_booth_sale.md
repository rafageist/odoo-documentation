<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events Booths Sales

- Scope: Community Addons
- Source: odoo/addons/event_booth_sale
- Dependencies: [[docs/Community Addons/event_booth/event_booth|event_booth]], [[docs/Community Addons/event_sale/event_sale|event_sale]]

## Summary

Manage event booths sale

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 6
- Views: 13
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4
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
title Events Booths Sales - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n13 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/event_booth_sale/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/event_booth_sale/Views|Views]] (6 files)
- Frontend: [[docs/Community Addons/event_booth_sale/Frontend|Frontend]] (2 files)

## Key models

- `account.move`
- `event.booth`
- `event.booth.category`
- `event.booth.configurator`
- `event.booth.registration`
- `event.type.booth`
- `product.product`
- `product.template`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






