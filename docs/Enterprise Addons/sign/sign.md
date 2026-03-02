<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sign

- Scope: Enterprise Addons
- Source: enterprise/sign
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/attachment_indexation/attachment_indexation|attachment_indexation]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/sms/sms|sms]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Send and request electronic signatures.

## Generated coverage

- Models: 24
- XML files with UI/data artifacts: 13
- Views: 31
- Actions: 13
- Menus: 11
- Rules (ir.rule): 25
- Access CSV entries: 19
- Controller units: 3
- Frontend asset files: 95

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
title Sign - Generated Coverage
component "Module Overview" as overview
component "Models\n24" as models
component "Views / XML\n31 views\n13 files" as views
component "Controllers\n23 routes" as controllers
component "Frontend\n95 files" as frontend
component "Security / Data\n25 rules\n19 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sign/Models|Models]] (24)
- Views and XML: [[docs/Enterprise Addons/sign/Views|Views]] (13 files)
- Controllers: [[docs/Enterprise Addons/sign/Controllers|Controllers]] (3)
- Frontend: [[docs/Enterprise Addons/sign/Frontend|Frontend]] (95 files)

## Key models

- `ir.http`
- `mail.activity.type`
- `report.sign.green_savings_report`
- `res.company`
- `res.config.settings`
- `res.partner`
- `res.users`
- `sign.completed.document`
- `sign.document`
- `sign.item`
- `sign.item.option`
- `sign.item.radio.set`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




