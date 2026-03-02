<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Marketing Automation

- Scope: Enterprise Addons
- Source: enterprise/marketing_automation
- Dependencies: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]

## Summary

Build automated mailing campaigns

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 11
- Views: 21
- Actions: 13
- Menus: 8
- Rules (ir.rule): 0
- Access CSV entries: 6
- Controller units: 0
- Frontend asset files: 14

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
title Marketing Automation - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n21 views\n11 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n14 files" as frontend
component "Security / Data\n0 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/marketing_automation/Models|Models]] (11)
- Views and XML: [[docs/Enterprise Addons/marketing_automation/Views|Views]] (11 files)
- Frontend: [[docs/Enterprise Addons/marketing_automation/Frontend|Frontend]] (14 files)

## Key models

- `mail.compose.message`
- `mailing.mailing`
- `mailing.trace`
- `mailing.trace.report`
- `marketing.activity`
- `marketing.campaign`
- `marketing.campaign.test`
- `marketing.participant`
- `marketing.trace`
- `utm.campaign`
- `utm.source`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





