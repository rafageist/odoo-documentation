<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT for PoS

- Scope: Enterprise Addons
- Source: enterprise/pos_iot
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Enterprise Addons/iot/iot|iot]]

## Summary

Use IoT Devices in the PoS

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 5
- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 20

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
title IoT for PoS - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n9 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n20 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/pos_iot/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/pos_iot/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/pos_iot/Frontend|Frontend]] (20 files)

## Key models

- `auto.config.pos.iot`
- `iot.box`
- `iot.device`
- `pos.config`
- `pos.payment.method`
- `pos.printer`
- `pos.session`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




