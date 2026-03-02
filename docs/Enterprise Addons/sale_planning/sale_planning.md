<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sale Planning

- Scope: Enterprise Addons
- Source: enterprise/sale_planning
- Dependencies: [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/sale_service/sale_service|sale_service]], [[docs/Enterprise Addons/planning/planning|planning]]

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 5
- Views: 16
- Actions: 10
- Menus: 1
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
title Sale Planning - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n16 views\n5 files" as views
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

- Models: [[docs/Enterprise Addons/sale_planning/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/sale_planning/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/sale_planning/Frontend|Frontend]] (5 files)

## Key models

- `planning.analysis.report`
- `planning.role`
- `planning.slot`
- `product.template`
- `sale.order`
- `sale.order.line`
- `uom.uom`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




