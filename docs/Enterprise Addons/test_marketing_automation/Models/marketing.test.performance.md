<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# marketing.test.performance

- Module: [[docs/Enterprise Addons/test_marketing_automation/test_marketing_automation|test_marketing_automation]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/test_models.py`
- Python classes: `MarketingTestPerformance`
- Description: MarketAuto: Model for performance check
- Inherits: `mail.thread.blacklist`, `mail.thread.phone`, `utm.mixin`

## Field footprint

- Detected fields: 7
- Field types: `Char` x 3, `Many2one` x 2, `Selection` x 1, `Text` x 1
- Relation fields: 2

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `customer_id`: `Many2one` (comodel `res.partner`)
- `description`: `Text`
- `email_from`: `Char` (compute `_compute_from_customer`, store `True`)
- `name`: `Char`
- `phone`: `Char` (compute `_compute_from_customer`, store `True`)
- `selection_field`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_from_customer`
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
title marketing.test.performance - Direct Relations
class "marketing.test.performance" as marketing_test_performance
class "res.company" as res_company
class "res.partner" as res_partner
marketing_test_performance --> res_company : company_id
marketing_test_performance --> res_partner : customer_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/test_marketing_automation/Models]]

<!-- GENERATED:MODEL -->
