<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Events Organization

- Scope: Community Addons
- Source: odoo/addons/event
- Dependencies: [[docs/Community Addons/barcodes/barcodes|barcodes]], [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/utm/utm|utm]]

## Summary

Trainings, Conferences, Meetings, Exhibitions, Registrations

## Generated coverage

- Models: 19
- XML files with UI/data artifacts: 16
- Views: 49
- Actions: 23
- Menus: 18
- Rules (ir.rule): 3
- Access CSV entries: 37
- Controller units: 1
- Frontend asset files: 19

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
title Events Organization - Generated Coverage
component "Module Overview" as overview
component "Models\n19" as models
component "Views / XML\n49 views\n16 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n19 files" as frontend
component "Security / Data\n3 rules\n37 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/event/Models|Models]] (19)
- Views and XML: [[docs/Community Addons/event/Views|Views]] (16 files)
- Controllers: [[docs/Community Addons/event/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/event/Frontend|Frontend]] (19 files)

## Key models

- `event.event`
- `event.event.ticket`
- `event.mail`
- `event.mail.registration`
- `event.mail.slot`
- `event.question`
- `event.question.answer`
- `event.registration`
- `event.registration.answer`
- `event.slot`
- `event.stage`
- `event.tag`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






