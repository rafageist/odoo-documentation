<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# POS Self Order IoT

- Scope: Enterprise Addons
- Source: enterprise/pos_self_order_iot
- Dependencies: [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]

## Summary

IoT in PoS Kiosk

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 2
- Views: 2
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
title POS Self Order IoT - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n4 routes" as controllers
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

- Models: [[docs/Enterprise Addons/pos_self_order_iot/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/pos_self_order_iot/Views|Views]] (2 files)
- Controllers: [[docs/Enterprise Addons/pos_self_order_iot/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/pos_self_order_iot/Frontend|Frontend]] (5 files)

## Key models

- `auto.config.pos.iot`
- `iot.box`
- `pos.config`
- `pos.payment.method`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




