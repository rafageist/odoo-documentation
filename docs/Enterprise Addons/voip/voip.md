<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Phone

- Scope: Enterprise Addons
- Source: enterprise/voip
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/web/web|web]], [[docs/Enterprise Addons/web_mobile/web_mobile|web_mobile]]

## Summary

Make and receive phone calls from within Odoo.

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 7
- Views: 12
- Actions: 3
- Menus: 5
- Rules (ir.rule): 4
- Access CSV entries: 6
- Controller units: 1
- Frontend asset files: 75

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
title Phone - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n12 views\n7 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n75 files" as frontend
component "Security / Data\n4 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/voip/Models|Models]] (9)
- Views and XML: [[docs/Enterprise Addons/voip/Views|Views]] (7 files)
- Controllers: [[docs/Enterprise Addons/voip/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/voip/Frontend|Frontend]] (75 files)

## Key models

- `mail.activity`
- `res.country`
- `res.partner`
- `res.users`
- `res.users.settings`
- `voip.call`
- `voip.country.code.mixin`
- `voip.provider`
- `voip.queue.mixin`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




