<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Forum on Courses

- Scope: Community Addons
- Source: odoo/addons/website_slides_forum
- Dependencies: [[docs/Community Addons/website_slides/website_slides|website_slides]], [[docs/Community Addons/website_forum/website_forum|website_forum]]

## Summary

Allows to link forum on a course

## Generated coverage

- Models: 2
- XML files with UI/data artifacts: 6
- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 9
- Access CSV entries: 1
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
title Forum on Courses - Generated Coverage
component "Module Overview" as overview
component "Models\n2" as models
component "Views / XML\n5 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n9 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_slides_forum/Models|Models]] (2)
- Views and XML: [[docs/Community Addons/website_slides_forum/Views|Views]] (6 files)
- Frontend: [[docs/Community Addons/website_slides_forum/Frontend|Frontend]] (2 files)

## Key models

- `forum.forum`
- `slide.channel`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





