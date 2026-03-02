<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# SMS Tests

- Scope: Community Addons
- Source: odoo/addons/test_mail_sms
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/sms/sms|sms]], [[docs/Community Addons/sms_twilio/sms_twilio|sms_twilio]], test_orm (not documented)

## Summary

SMS Tests: performances and tests specific to SMS

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 13
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
title SMS Tests - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n13 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/test_mail_sms/Models|Models]] (7)

## Key models

- `mail.test.sms`
- `mail.test.sms.bl`
- `mail.test.sms.bl.activity`
- `mail.test.sms.bl.optout`
- `mail.test.sms.partner`
- `mail.test.sms.partner.2many`
- `sms.test.nothread`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





