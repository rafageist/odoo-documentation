
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Online Event Ticketing

- Scope: Community Addons
- Source: odoo/addons/website_event_sale
- Dependencies: [[docs/Community Addons/website_event/website_event|website_event]], [[docs/Community Addons/event_sale/event_sale|event_sale]], [[docs/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Sell event tickets online

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 2
- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
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
title Online Event Ticketing - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n2 views\n2 files" as views
component "Controllers\n1 routes" as controllers
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

- Models: [[docs/Community Addons/website_event_sale/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/website_event_sale/Views|Views]] (2 files)
- Controllers: [[docs/Community Addons/website_event_sale/Controllers|Controllers]] (1)

## Key models

- `event.sale.report`
- `product.pricelist.item`
- `product.product`
- `product.template`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


