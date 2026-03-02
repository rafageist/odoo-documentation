<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Databases

- Scope: Enterprise Addons
- Source: enterprise/databases
- Dependencies: [[docs/Community Addons/project/project|project]]

## Summary

Manage a fleet of Odoo databases

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 7
- Views: 6
- Actions: 7
- Menus: 5
- Rules (ir.rule): 3
- Access CSV entries: 4
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
title Databases - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n6 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n3 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/databases/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/databases/Views|Views]] (7 files)
- Frontend: [[docs/Enterprise Addons/databases/Frontend|Frontend]] (2 files)

## Key models

- `databases.manage_users.wizard`
- `databases.synchronization.wizard`
- `databases.user`
- `project.project`
- `project.template.create.wizard`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



