<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Point of Sale Restaurant Appointment

- Scope: Enterprise Addons
- Source: enterprise/pos_restaurant_appointment
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Enterprise Addons/pos_appointment/pos_appointment|pos_appointment]]

## Summary

This module lets you manage online reservations for restaurant tables

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 9

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
title Point of Sale Restaurant Appointment - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_restaurant_appointment/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/pos_restaurant_appointment/Views|Views]] (3 files)
- Frontend: [[docs/Enterprise Addons/pos_restaurant_appointment/Frontend|Frontend]] (9 files)

## Key models

- `appointment.resource`
- `calendar.event`
- `pos.session`
- `restaurant.table`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




