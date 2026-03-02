<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events Sales

- Scope: Community Addons
- Source: odoo/addons/event_sale
- Dependencies: [[docs/Community Addons/event_product/event_product|event_product]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 8
- Views: 12
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 4
- Controller units: 0
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
title Events Sales - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n12 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n1 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/event_sale/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/event_sale/Views|Views]] (8 files)
- Frontend: [[docs/Community Addons/event_sale/Frontend|Frontend]] (3 files)

## Key models

- `event.event`
- `event.event.configurator`
- `event.event.ticket`
- `event.registration`
- `event.sale.report`
- `product.template`
- `registration.editor`
- `registration.editor.line`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






