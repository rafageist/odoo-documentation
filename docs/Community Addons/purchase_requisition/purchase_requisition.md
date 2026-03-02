<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Purchase Agreements

- Scope: Community Addons
- Source: odoo/addons/purchase_requisition
- Dependencies: [[docs/Community Addons/purchase/purchase|purchase]]

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 8
- Views: 12
- Actions: 4
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 7
- Controller units: 0
- Frontend asset files: 4

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
title Purchase Agreements - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n12 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n2 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/purchase_requisition/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/purchase_requisition/Views|Views]] (8 files)
- Frontend: [[docs/Community Addons/purchase_requisition/Frontend|Frontend]] (4 files)

## Key models

- `product.product`
- `product.supplierinfo`
- `purchase.order`
- `purchase.order.group`
- `purchase.order.line`
- `purchase.requisition`
- `purchase.requisition.alternative.warning`
- `purchase.requisition.create.alternative`
- `purchase.requisition.line`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






