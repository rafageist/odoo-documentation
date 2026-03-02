<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Point of Sale online payment

- Scope: Community Addons
- Source: odoo/addons/pos_online_payment
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/account_payment/account_payment|account_payment]]

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 5
- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 9

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
title Point of Sale online payment - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n6 views\n5 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/pos_online_payment/Models|Models]] (7)
- Views and XML: [[docs/Community Addons/pos_online_payment/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/pos_online_payment/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/pos_online_payment/Frontend|Frontend]] (9 files)

## Key models

- `account.payment`
- `payment.transaction`
- `pos.config`
- `pos.order`
- `pos.payment`
- `pos.payment.method`
- `pos.session`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






