<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events

- Scope: Community Addons
- Source: odoo/addons/website_event
- Dependencies: [[docs/Community Addons/event/event|event]], [[docs/Community Addons/website/website|website]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Publish events, sell tickets

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 12
- Views: 19
- Actions: 6
- Menus: 2
- Rules (ir.rule): 8
- Access CSV entries: 27
- Controller units: 2
- Frontend asset files: 22

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
title Events - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n19 views\n12 files" as views
component "Controllers\n9 routes" as controllers
component "Frontend\n22 files" as frontend
component "Security / Data\n8 rules\n27 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_event/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/website_event/Views|Views]] (12 files)
- Controllers: [[docs/Community Addons/website_event/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_event/Frontend|Frontend]] (22 files)

## Key models

- `event.event`
- `event.registration`
- `event.tag`
- `event.tag.category`
- `event.type`
- `website`
- `website.event.menu`
- `website.menu`
- `website.snippet.filter`
- `website.visitor`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




