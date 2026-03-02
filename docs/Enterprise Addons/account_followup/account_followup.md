<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payment Follow-up Management

- Scope: Enterprise Addons
- Source: enterprise/account_followup
- Dependencies: [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/sms/sms|sms]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 10
- Views: 11
- Actions: 5
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 7
- Controller units: 0
- Frontend asset files: 3

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
title Payment Follow-up Management - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n11 views\n10 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n2 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_followup/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/account_followup/Views|Views]] (10 files)
- Frontend: [[docs/Enterprise Addons/account_followup/Frontend|Frontend]] (3 files)

## Key models

- `account.followup.report`
- `account.move.line`
- `account_followup.followup.line`
- `account_followup.manual_reminder`
- `account_followup.missing.information.wizard`
- `ir.actions.report`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





