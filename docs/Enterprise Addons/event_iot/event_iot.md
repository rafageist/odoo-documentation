<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT for Events

- Scope: Enterprise Addons
- Source: enterprise/event_iot
- Dependencies: [[docs/Enterprise Addons/iot/iot|iot]], [[docs/Community Addons/event/event|event]]

## Summary

Use IoT device integrations for events

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 1
- Views: 0
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title IoT for Events - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n0 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/event_iot/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/event_iot/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/event_iot/Frontend|Frontend]] (2 files)

## Key models

- `event.event`
- `event.registration`
- `report.event_iot.event_registration_badge_printer_report`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




