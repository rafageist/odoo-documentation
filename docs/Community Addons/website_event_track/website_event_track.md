
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Advanced Events

- Scope: Community Addons
- Source: odoo/addons/website_event_track
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]]

## Summary

Sponsors, Tracks, Agenda, Event News

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 11
- Views: 26
- Actions: 9
- Menus: 6
- Rules (ir.rule): 2
- Access CSV entries: 19
- Controller units: 2
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
title Advanced Events - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n26 views\n11 files" as views
component "Controllers\n12 routes" as controllers
component "Frontend\n15 files" as frontend
component "Security / Data\n2 rules\n19 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_event_track/Models|Models]] (13)
- Views and XML: [[docs/Community Addons/website_event_track/Views|Views]] (11 files)
- Controllers: [[docs/Community Addons/website_event_track/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_event_track/Frontend|Frontend]] (15 files)

## Key models

- `event.event`
- `event.track`
- `event.track.location`
- `event.track.stage`
- `event.track.tag`
- `event.track.tag.category`
- `event.track.visitor`
- `event.type`
- `res.config.settings`
- `website`
- `website.event.menu`
- `website.menu`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


