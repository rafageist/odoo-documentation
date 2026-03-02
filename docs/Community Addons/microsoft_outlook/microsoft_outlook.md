<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Microsoft Outlook

- Scope: Community Addons
- Source: odoo/addons/microsoft_outlook
- Dependencies: [[docs/Community Addons/mail/mail|mail]]

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
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
title Microsoft Outlook - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/microsoft_outlook/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/microsoft_outlook/Views|Views]] (3 files)
- Controllers: [[docs/Community Addons/microsoft_outlook/Controllers|Controllers]] (1)

## Key models

- `fetchmail.server`
- `ir.mail_server`
- `microsoft.outlook.mixin`
- `res.config.settings`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






