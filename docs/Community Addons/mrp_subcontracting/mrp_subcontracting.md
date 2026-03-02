<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# MRP Subcontracting

- Scope: Community Addons
- Source: odoo/addons/mrp_subcontracting
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]]

## Summary

Subcontract Productions

## Generated coverage

- Models: 18
- XML files with UI/data artifacts: 10
- Views: 20
- Actions: 1
- Menus: 0
- Rules (ir.rule): 13
- Access CSV entries: 16
- Controller units: 1
- Frontend asset files: 13

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
title MRP Subcontracting - Generated Coverage
component "Module Overview" as overview
component "Models\n18" as models
component "Views / XML\n20 views\n10 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n13 files" as frontend
component "Security / Data\n13 rules\n16 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mrp_subcontracting/Models|Models]] (18)
- Views and XML: [[docs/Community Addons/mrp_subcontracting/Views|Views]] (10 files)
- Controllers: [[docs/Community Addons/mrp_subcontracting/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/mrp_subcontracting/Frontend|Frontend]] (13 files)

## Key models

- `change.production.qty`
- `mrp.bom`
- `mrp.production`
- `mrp.production.serials`
- `product.product`
- `product.supplierinfo`
- `report.mrp.report_bom_structure`
- `res.company`
- `res.partner`
- `stock.location`
- `stock.move`
- `stock.move.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






