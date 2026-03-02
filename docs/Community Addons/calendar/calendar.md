<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Calendar

- Scope: Community Addons
- Source: odoo/addons/calendar
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]]

## Summary

Schedule employees' meetings

## Generated coverage

- Models: 18
- XML files with UI/data artifacts: 9
- Views: 18
- Actions: 8
- Menus: 8
- Rules (ir.rule): 4
- Access CSV entries: 15
- Controller units: 1
- Frontend asset files: 43

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
title Calendar - Generated Coverage
component "Module Overview" as overview
component "Models\n18" as models
component "Views / XML\n18 views\n9 files" as views
component "Controllers\n10 routes" as controllers
component "Frontend\n43 files" as frontend
component "Security / Data\n4 rules\n15 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/calendar/Models|Models]] (18)
- Views and XML: [[docs/Community Addons/calendar/Views|Views]] (9 files)
- Controllers: [[docs/Community Addons/calendar/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/calendar/Frontend|Frontend]] (43 files)

## Key models

- `calendar.alarm`
- `calendar.alarm_manager`
- `calendar.attendee`
- `calendar.event`
- `calendar.event.type`
- `calendar.filters`
- `calendar.popover.delete.wizard`
- `calendar.provider.config`
- `calendar.recurrence`
- `discuss.channel`
- `ir.http`
- `mail.activity`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






