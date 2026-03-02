<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Marketing Automation Tests

- Scope: Enterprise Addons
- Source: enterprise/test_marketing_automation
- Dependencies: [[docs/Enterprise Addons/marketing_automation/marketing_automation|marketing_automation]], [[docs/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]], [[docs/Enterprise Addons/marketing_automation_whatsapp/marketing_automation_whatsapp|marketing_automation_whatsapp]], [[docs/Community Addons/test_mail/test_mail|test_mail]], [[docs/Enterprise Addons/test_mail_enterprise/test_mail_enterprise|test_mail_enterprise]], [[docs/Community Addons/test_mail_full/test_mail_full|test_mail_full]], [[docs/Community Addons/test_mail_sms/test_mail_sms|test_mail_sms]], [[docs/Community Addons/test_mass_mailing/test_mass_mailing|test_mass_mailing]]

## Summary

Test Suite for Automated Marketing Campaigns

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4
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
title Marketing Automation Tests - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/test_marketing_automation/Models|Models]] (4)

## Key models

- `marketing.test`
- `marketing.test.performance`
- `marketing.test.sms`
- `marketing.test.utm`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





