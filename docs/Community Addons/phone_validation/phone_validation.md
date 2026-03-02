<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Phone Numbers Validation

- Scope: Community Addons
- Source: odoo/addons/phone_validation
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]]

## Summary

Validate and format phone numbers

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 3
- Views: 5
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3
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
title Phone Numbers Validation - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n5 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/phone_validation/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/phone_validation/Views|Views]] (3 files)

## Key models

- `base`
- `mail.thread.phone`
- `phone.blacklist`
- `phone.blacklist.remove`
- `res.partner`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






