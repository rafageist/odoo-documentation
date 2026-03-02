<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Project Planning

- Scope: Enterprise Addons
- Source: enterprise/project_forecast
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Enterprise Addons/planning/planning|planning]], [[docs/Enterprise Addons/web_grid/web_grid|web_grid]]

## Summary

Plan your resources on project tasks

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 5
- Views: 16
- Actions: 23
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 4

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
title Project Planning - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n16 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n3 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/project_forecast/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/project_forecast/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/project_forecast/Frontend|Frontend]] (4 files)

## Key models

- `planning.analysis.report`
- `planning.slot`
- `planning.slot.template`
- `project.project`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




