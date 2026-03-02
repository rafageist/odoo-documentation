<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# IoT for Delivery

- Scope: Enterprise Addons
- Source: enterprise/delivery_iot
- Dependencies: [[docs/Enterprise Addons/iot/iot|iot]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Use IoT devices in delivery operations

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 5
- Views: 3
- Actions: 2
- Menus: 4
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title IoT for Delivery - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n3 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/delivery_iot/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/delivery_iot/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/delivery_iot/Frontend|Frontend]] (2 files)

## Key models

- `iot.device`
- `ir.actions.report`
- `stock.picking`
- `stock.picking.type`
- `stock.put.in.pack`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




