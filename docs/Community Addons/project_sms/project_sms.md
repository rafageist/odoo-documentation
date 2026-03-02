<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project - SMS

- Scope: Community Addons
- Source: odoo/addons/project_sms
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Send text messages when project/task stage move

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 5
- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 0

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
title Project - SMS - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n6 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/project_sms/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/project_sms/Views|Views]] (5 files)

## Key models

- `project.project`
- `project.project.stage`
- `project.task`
- `project.task.type`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






