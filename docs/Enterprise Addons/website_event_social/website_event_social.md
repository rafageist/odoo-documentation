<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Schedule push notifications on attendees

- Scope: Enterprise Addons
- Source: enterprise/website_event_social
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Enterprise Addons/social_push_notifications/social_push_notifications|social_push_notifications]]

## Summary

Bridge module to push notifications to event attendees

## Generated coverage

- Models: 2
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 1

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
title Schedule push notifications on attendees - Generated Coverage
component "Module Overview" as overview
component "Models\n2" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_event_social/Models|Models]] (2)
- Views and XML: [[docs/Enterprise Addons/website_event_social/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/website_event_social/Frontend|Frontend]] (1 files)

## Key models

- `event.event`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




