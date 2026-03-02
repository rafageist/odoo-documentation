<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp Messaging

- Scope: Enterprise Addons
- Source: enterprise/whatsapp
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]

## Summary

Text your Contacts on WhatsApp

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 14
- Views: 22
- Actions: 5
- Menus: 5
- Rules (ir.rule): 14
- Access CSV entries: 14
- Controller units: 0
- Frontend asset files: 39

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
title WhatsApp Messaging - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n22 views\n14 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n39 files" as frontend
component "Security / Data\n14 rules\n14 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/whatsapp/Models|Models]] (15)
- Views and XML: [[docs/Enterprise Addons/whatsapp/Views|Views]] (14 files)
- Frontend: [[docs/Enterprise Addons/whatsapp/Frontend|Frontend]] (39 files)

## Key models

- `base`
- `discuss.channel`
- `discuss.channel.member`
- `ir.actions.server`
- `mail.message`
- `mail.thread`
- `res.partner`
- `res.users.settings`
- `whatsapp.account`
- `whatsapp.composer`
- `whatsapp.message`
- `whatsapp.preview`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




