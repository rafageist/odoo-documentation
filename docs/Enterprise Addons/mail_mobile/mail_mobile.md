<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Mail Mobile

- Scope: Enterprise Addons
- Source: enterprise/mail_mobile
- Dependencies: [[docs/Community Addons/iap_mail/iap_mail|iap_mail]], [[docs/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[docs/Enterprise Addons/web_mobile/web_mobile|web_mobile]], [[docs/Community Addons/base_setup/base_setup|base_setup]]

## Summary

Provides push notification and redirection to the mobile app.

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
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
title Mail Mobile - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/mail_mobile/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/mail_mobile/Views|Views]] (1 files)
- Frontend: [[docs/Enterprise Addons/mail_mobile/Frontend|Frontend]] (1 files)

## Key models

- `discuss.channel`
- `ir.http`
- `mail.thread`
- `res.config.settings`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




