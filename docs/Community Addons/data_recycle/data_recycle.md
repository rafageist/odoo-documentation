<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Data Recycle

- Scope: Community Addons
- Source: odoo/addons/data_recycle
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

## Summary

Find old records and archive/delete them

## Generated coverage

- Models: 2
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 3
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 2
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
title Data Recycle - Generated Coverage
component "Module Overview" as overview
component "Models\n2" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/data_recycle/Models|Models]] (2)
- Views and XML: [[docs/Community Addons/data_recycle/Views|Views]] (3 files)
- Frontend: [[docs/Community Addons/data_recycle/Frontend|Frontend]] (3 files)

## Key models

- `data_recycle.model`
- `data_recycle.record`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






