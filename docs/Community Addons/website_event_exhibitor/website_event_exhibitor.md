<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Event Exhibitors

- Scope: Community Addons
- Source: odoo/addons/website_event_exhibitor
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]]

## Summary

Event: manage sponsors and exhibitors

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 5
- Views: 9
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 5
- Controller units: 1
- Frontend asset files: 5

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
title Event Exhibitors - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n9 views\n5 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n1 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_event_exhibitor/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/website_event_exhibitor/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/website_event_exhibitor/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_event_exhibitor/Frontend|Frontend]] (5 files)

## Key models

- `event.event`
- `event.sponsor`
- `event.sponsor.type`
- `event.type`
- `website`
- `website.event.menu`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






