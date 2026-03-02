<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# PoS Order Tracking Customer Display

- Scope: Enterprise Addons
- Source: enterprise/pos_order_tracking_display
- Dependencies: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]], [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

## Summary

Display customer's order status

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 5

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
title PoS Order Tracking Customer Display - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_order_tracking_display/Models|Models]] (3)
- Views and XML: [[docs/Enterprise Addons/pos_order_tracking_display/Views|Views]] (1 files)
- Controllers: [[docs/Enterprise Addons/pos_order_tracking_display/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/pos_order_tracking_display/Frontend|Frontend]] (5 files)

## Key models

- `ir.http`
- `pos.prep.display`
- `pos.prep.state`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





