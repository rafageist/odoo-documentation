<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - Sales

- Scope: Community Addons
- Source: odoo/addons/pos_sale
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Link module between Point of Sale and Sales

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 5
- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 8

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
title POS - Sales - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n5 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n8 files" as frontend
component "Security / Data\n1 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/pos_sale/Models|Models]] (13)
- Views and XML: [[docs/Community Addons/pos_sale/Views|Views]] (5 files)
- Frontend: [[docs/Community Addons/pos_sale/Frontend|Frontend]] (8 files)

## Key models

- `account.move`
- `crm.team`
- `pos.config`
- `pos.order`
- `pos.order.line`
- `pos.session`
- `product.template`
- `res.config.settings`
- `res.partner`
- `sale.order`
- `sale.order.line`
- `sale.report`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






