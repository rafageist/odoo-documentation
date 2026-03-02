<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Purchase and Subcontracting Management

- Scope: Community Addons
- Source: odoo/addons/mrp_subcontracting_purchase
- Dependencies: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]], [[docs/Community Addons/purchase_mrp/purchase_mrp|purchase_mrp]]

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 0

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
title Purchase and Subcontracting Management - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mrp_subcontracting_purchase/Models|Models]] (7)
- Views and XML: [[docs/Community Addons/mrp_subcontracting_purchase/Views|Views]] (2 files)

## Key models

- `account.move.line`
- `product.product`
- `purchase.order`
- `report.mrp.report_bom_structure`
- `stock.move`
- `stock.picking`
- `stock.rule`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






