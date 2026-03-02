<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Fleet

- Scope: Community Addons
- Source: odoo/addons/fleet
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]]

## Summary

Manage your fleet and track car costs

## Generated coverage

- Models: 16
- XML files with UI/data artifacts: 9
- Views: 51
- Actions: 15
- Menus: 21
- Rules (ir.rule): 9
- Access CSV entries: 24
- Controller units: 0
- Frontend asset files: 1

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
title Fleet - Generated Coverage
component "Module Overview" as overview
component "Models\n16" as models
component "Views / XML\n51 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n9 rules\n24 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/fleet/Models|Models]] (16)
- Views and XML: [[docs/Community Addons/fleet/Views|Views]] (9 files)
- Frontend: [[docs/Community Addons/fleet/Frontend|Frontend]] (1 files)

## Key models

- `fleet.service.type`
- `fleet.vehicle`
- `fleet.vehicle.assignation.log`
- `fleet.vehicle.cost.report`
- `fleet.vehicle.log.contract`
- `fleet.vehicle.log.services`
- `fleet.vehicle.model`
- `fleet.vehicle.model.brand`
- `fleet.vehicle.model.category`
- `fleet.vehicle.odometer`
- `fleet.vehicle.odometer.report`
- `fleet.vehicle.send.mail`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






