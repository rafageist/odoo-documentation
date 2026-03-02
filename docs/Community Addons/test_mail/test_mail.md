<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Tests

- Scope: Community Addons
- Source: odoo/addons/test_mail
- Dependencies: [[docs/Community Addons/mail/mail|mail]], test_orm (not documented)

## Summary

Mail Tests: performances and tests specific to mail

## Generated coverage

- Models: 47
- XML files with UI/data artifacts: 1
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 19
- Access CSV entries: 77
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
title Mail Tests - Generated Coverage
component "Module Overview" as overview
component "Models\n47" as models
component "Views / XML\n0 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n19 rules\n77 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/test_mail/Models|Models]] (47)
- Views and XML: [[docs/Community Addons/test_mail/Views|Views]] (1 files)

## Key models

- `mail.performance.thread`
- `mail.performance.thread.recipients`
- `mail.performance.tracking`
- `mail.test.access`
- `mail.test.access.custo`
- `mail.test.access.public`
- `mail.test.activity`
- `mail.test.alias.optional`
- `mail.test.cc`
- `mail.test.composer.mixin`
- `mail.test.composer.source`
- `mail.test.container`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





