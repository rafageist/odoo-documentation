
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Product Lifecycle Management (PLM)

- Scope: Enterprise Addons
- Source: enterprise/mrp_plm
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]]

## Summary

Manage engineering change orders on products, bills of material

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 6
- Views: 25
- Actions: 13
- Menus: 14
- Rules (ir.rule): 1
- Access CSV entries: 13
- Controller units: 0
- Frontend asset files: 11

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
title Product Lifecycle Management (PLM) - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n25 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n1 rules\n13 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/mrp_plm/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/mrp_plm/Views|Views]] (6 files)
- Frontend: [[docs/Enterprise Addons/mrp_plm/Frontend|Frontend]] (11 files)

## Key models

- `mrp.bom`
- `mrp.bom.byproduct`
- `mrp.bom.line`
- `mrp.eco`
- `mrp.eco.approval`
- `mrp.eco.approval.template`
- `mrp.eco.bom.change`
- `mrp.eco.routing.change`
- `mrp.eco.stage`
- `mrp.eco.tag`
- `mrp.eco.type`
- `mrp.production`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


