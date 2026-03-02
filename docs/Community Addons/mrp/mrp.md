<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Manufacturing

- Scope: Community Addons
- Source: odoo/addons/mrp
- Dependencies: [[docs/Community Addons/product/product|product]], [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/resource/resource|resource]]

## Summary

Manufacturing Orders & BOMs

## Generated coverage

- Models: 51
- XML files with UI/data artifacts: 27
- Views: 85
- Actions: 61
- Menus: 21
- Rules (ir.rule): 9
- Access CSV entries: 54
- Controller units: 0
- Frontend asset files: 46

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
title Manufacturing - Generated Coverage
component "Module Overview" as overview
component "Models\n51" as models
component "Views / XML\n85 views\n27 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n46 files" as frontend
component "Security / Data\n9 rules\n54 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mrp/Models|Models]] (51)
- Views and XML: [[docs/Community Addons/mrp/Views|Views]] (27 files)
- Frontend: [[docs/Community Addons/mrp/Frontend|Frontend]] (46 files)

## Key models

- `change.production.qty`
- `ir.attachment`
- `mrp.bom`
- `mrp.bom.byproduct`
- `mrp.bom.line`
- `mrp.consumption.warning`
- `mrp.consumption.warning.line`
- `mrp.production`
- `mrp.production.backorder`
- `mrp.production.backorder.line`
- `mrp.production.group`
- `mrp.production.serials`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






