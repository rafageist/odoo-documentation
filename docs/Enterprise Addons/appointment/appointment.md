<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Appointments

- Scope: Enterprise Addons
- Source: enterprise/appointment
- Dependencies: [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/resource/resource|resource]], [[docs/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Allow people to book meetings in your agenda

## Generated coverage

- Models: 14
- XML files with UI/data artifacts: 14
- Views: 38
- Actions: 14
- Menus: 16
- Rules (ir.rule): 13
- Access CSV entries: 29
- Controller units: 5
- Frontend asset files: 57

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
title Appointments - Generated Coverage
component "Module Overview" as overview
component "Models\n14" as models
component "Views / XML\n38 views\n14 files" as views
component "Controllers\n25 routes" as controllers
component "Frontend\n57 files" as frontend
component "Security / Data\n13 rules\n29 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/appointment/Models|Models]] (14)
- Views and XML: [[docs/Enterprise Addons/appointment/Views|Views]] (14 files)
- Controllers: [[docs/Enterprise Addons/appointment/Controllers|Controllers]] (5)
- Frontend: [[docs/Enterprise Addons/appointment/Frontend|Frontend]] (57 files)

## Key models

- `appointment.answer`
- `appointment.answer.input`
- `appointment.booking.line`
- `appointment.invite`
- `appointment.manage.leaves`
- `appointment.question`
- `appointment.resource`
- `appointment.slot`
- `appointment.type`
- `calendar.alarm`
- `calendar.attendee`
- `calendar.event`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





