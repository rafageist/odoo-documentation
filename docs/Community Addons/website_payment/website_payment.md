<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Website Payment

- Scope: Community Addons
- Source: odoo/addons/website_payment
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/portal/portal|portal]]

## Summary

Payment integration with website

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 2
- Frontend asset files: 12

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
title Website Payment - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n12 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_payment/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/website_payment/Views|Views]] (2 files)
- Controllers: [[docs/Community Addons/website_payment/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_payment/Frontend|Frontend]] (12 files)

## Key models

- `account.payment`
- `payment.provider`
- `payment.transaction`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




