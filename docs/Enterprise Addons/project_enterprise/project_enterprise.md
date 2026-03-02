<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Project Enterprise

- Scope: Enterprise Addons
- Source: enterprise/project_enterprise
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Enterprise Addons/web_map/web_map|web_map]], [[docs/Enterprise Addons/web_gantt/web_gantt|web_gantt]], [[docs/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]]

## Summary

Bridge module for project and enterprise

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 26
- Actions: 21
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 47

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
title Project Enterprise - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n26 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n47 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/project_enterprise/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/project_enterprise/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/project_enterprise/Frontend|Frontend]] (47 files)

## Key models

- `project.project`
- `project.task`
- `project.task.recurrence`
- `report.project.task.user`
- `res.users`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




