<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sms.composer

- Module: [[docs/Enterprise Addons/marketing_automation_sms/marketing_automation_sms|marketing_automation_sms]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `wizard/sms_composer.py`
- Python classes: `SmsComposer`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `marketing_activity_id`: `Many2one` (comodel `marketing.activity`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Direct relation diagram

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
title sms.composer - Direct Relations
class "sms.composer" as sms_composer
class "marketing.activity" as marketing_activity
sms_composer --> marketing_activity : marketing_activity_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/marketing_automation_sms/Models]]

<!-- GENERATED:MODEL -->
