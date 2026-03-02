<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Group

- Scope: Community Addons
- Source: odoo/addons/mail_group
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/portal/portal|portal]]

## Summary

Manage your mailing lists

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 8
- Views: 12
- Actions: 6
- Menus: 2
- Rules (ir.rule): 10
- Access CSV entries: 9
- Controller units: 1
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
title Mail Group - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n12 views\n8 files" as views
component "Controllers\n9 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n10 rules\n9 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mail_group/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/mail_group/Views|Views]] (8 files)
- Controllers: [[docs/Community Addons/mail_group/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/mail_group/Frontend|Frontend]] (2 files)

## Key models

- `mail.group`
- `mail.group.member`
- `mail.group.message`
- `mail.group.message.reject`
- `mail.group.moderation`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






