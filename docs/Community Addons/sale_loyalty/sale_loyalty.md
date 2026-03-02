<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sale Loyalty

- Scope: Community Addons
- Source: odoo/addons/sale_loyalty
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/loyalty/loyalty|loyalty]]

## Summary

Use discounts and loyalty programs in sales orders

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 7
- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 17
- Controller units: 0
- Frontend asset files: 2

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
title Sale Loyalty - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n6 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n17 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/sale_loyalty/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/sale_loyalty/Views|Views]] (7 files)
- Frontend: [[docs/Community Addons/sale_loyalty/Frontend|Frontend]] (2 files)

## Key models

- `loyalty.card`
- `loyalty.history`
- `loyalty.program`
- `loyalty.reward`
- `sale.loyalty.coupon.wizard`
- `sale.loyalty.reward.wizard`
- `sale.order`
- `sale.order.coupon.points`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





