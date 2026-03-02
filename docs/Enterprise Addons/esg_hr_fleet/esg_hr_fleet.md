<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# ESG HR Fleet

- Scope: Enterprise Addons
- Source: enterprise/esg_hr_fleet
- Dependencies: [[docs/Enterprise Addons/esg/esg|esg]], [[docs/Community Addons/hr_fleet/hr_fleet|hr_fleet]]

## Summary

Measure fleet emissions based on your employees' commuting distance and vehicle data.

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 5
- Views: 4
- Actions: 3
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 2
- Controller units: 0
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
title ESG HR Fleet - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n4 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n1 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/esg_hr_fleet/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/esg_hr_fleet/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/esg_hr_fleet/Frontend|Frontend]] (5 files)

## Key models

- `employee.commuting.emissions.wizard`
- `esg.employee.commuting.report`
- `esg.other.emission`
- `fleet.vehicle.assignation.log`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




