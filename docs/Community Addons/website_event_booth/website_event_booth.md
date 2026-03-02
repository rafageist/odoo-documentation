
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Online Event Booths

- Scope: Community Addons
- Source: odoo/addons/website_event_booth
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Community Addons/event_booth/event_booth|event_booth]]

## Summary

Events, display your booths on your website

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 3
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4
- Controller units: 1
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
title Online Event Booths - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n2 views\n3 files" as views
component "Controllers\n6 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n1 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_event_booth/Models|Models]] (3)
- Views and XML: [[docs/Community Addons/website_event_booth/Views|Views]] (3 files)
- Controllers: [[docs/Community Addons/website_event_booth/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_event_booth/Frontend|Frontend]] (2 files)

## Key models

- `event.event`
- `event.type`
- `website.event.menu`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


