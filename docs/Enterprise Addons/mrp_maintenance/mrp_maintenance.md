<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Maintenance - MRP

- Scope: Enterprise Addons
- Source: enterprise/mrp_maintenance
- Dependencies: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[docs/Community Addons/stock_maintenance/stock_maintenance|stock_maintenance]]

## Summary

Schedule and manage maintenance on machine and tools.

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 2
- Views: 11
- Actions: 3
- Menus: 3
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
title Maintenance - MRP - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n11 views\n2 files" as views
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

- Models: [[docs/Enterprise Addons/mrp_maintenance/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/mrp_maintenance/Views|Views]] (2 files)
- Frontend: [[docs/Enterprise Addons/mrp_maintenance/Frontend|Frontend]] (2 files)

## Key models

- `maintenance.equipment`
- `maintenance.request`
- `maintenance.stage`
- `mrp.production`
- `mrp.workcenter`
- `mrp.workorder`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




