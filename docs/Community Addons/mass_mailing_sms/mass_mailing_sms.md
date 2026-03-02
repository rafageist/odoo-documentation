<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# SMS Marketing

- Scope: Community Addons
- Source: odoo/addons/mass_mailing_sms
- Dependencies: [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Design, send and track SMS

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 9
- Views: 23
- Actions: 10
- Menus: 10
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 1
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
title SMS Marketing - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n23 views\n9 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mass_mailing_sms/Models|Models]] (11)
- Views and XML: [[docs/Community Addons/mass_mailing_sms/Views|Views]] (9 files)
- Controllers: [[docs/Community Addons/mass_mailing_sms/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/mass_mailing_sms/Frontend|Frontend]] (1 files)

## Key models

- `mailing.contact`
- `mailing.list`
- `mailing.mailing`
- `mailing.sms.test`
- `mailing.trace`
- `res.users`
- `sms.composer`
- `sms.sms`
- `sms.tracker`
- `utm.campaign`
- `utm.medium`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






