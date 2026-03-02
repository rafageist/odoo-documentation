<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Onboarding Toolbox

- Scope: Community Addons
- Source: odoo/addons/onboarding
- Dependencies: [[docs/Community Addons/web/web|web]]

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 2
- Views: 4
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 12
- Controller units: 0
- Frontend asset files: 1

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
title Onboarding Toolbox - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n4 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n12 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/onboarding/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/onboarding/Views|Views]] (2 files)
- Frontend: [[docs/Community Addons/onboarding/Frontend|Frontend]] (1 files)

## Key models

- `onboarding.onboarding`
- `onboarding.onboarding.step`
- `onboarding.progress`
- `onboarding.progress.step`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






