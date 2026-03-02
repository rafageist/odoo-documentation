<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Remote Work

- Scope: Community Addons
- Source: odoo/addons/hr_homeworking
- Dependencies: [[docs/Community Addons/hr/hr|hr]]

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 3
- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
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
title Remote Work - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n5 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n2 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/hr_homeworking/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/hr_homeworking/Views|Views]] (3 files)
- Frontend: [[docs/Community Addons/hr_homeworking/Frontend|Frontend]] (3 files)

## Key models

- `hr.employee`
- `hr.employee.location`
- `hr.employee.public`
- `hr.work.location`
- `res.partner`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






