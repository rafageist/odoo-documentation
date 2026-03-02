<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# SMS Marketing in Marketing Automation

- Scope: Enterprise Addons
- Source: enterprise/marketing_automation_sms
- Dependencies: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]

## Summary

Integrate SMS Marketing in marketing campaigns

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 6
- Views: 7
- Actions: 4
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1
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
title SMS Marketing in Marketing Automation - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n7 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/marketing_automation_sms/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/marketing_automation_sms/Views|Views]] (6 files)

## Key models

- `mailing.mailing`
- `mailing.trace`
- `marketing.activity`
- `marketing.campaign`
- `marketing.trace`
- `sms.composer`
- `sms.tracker`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





