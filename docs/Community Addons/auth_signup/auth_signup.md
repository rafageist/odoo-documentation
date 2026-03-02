<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Signup

- Scope: Community Addons
- Source: odoo/addons/auth_signup
- Dependencies: [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/web/web|web]]

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 2
- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 2
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
title Signup - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n3 views\n2 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/auth_signup/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/auth_signup/Views|Views]] (2 files)
- Controllers: [[docs/Community Addons/auth_signup/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/auth_signup/Frontend|Frontend]] (1 files)

## Key models

- `ir.http`
- `res.config.settings`
- `res.partner`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






