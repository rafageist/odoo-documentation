<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sell Courses

- Scope: Community Addons
- Source: odoo/addons/website_sale_slides
- Dependencies: [[docs/Community Addons/website_slides/website_slides|website_slides]], [[docs/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell your courses online

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 4
- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 7

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
title Sell Courses - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n6 views\n4 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n7 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_slides/Models|Models]] (5)
- Views and XML: [[docs/Community Addons/website_sale_slides/Views|Views]] (4 files)
- Controllers: [[docs/Community Addons/website_sale_slides/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_sale_slides/Frontend|Frontend]] (7 files)

## Key models

- `product.product`
- `product.template`
- `sale.order`
- `sale.order.line`
- `slide.channel`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





