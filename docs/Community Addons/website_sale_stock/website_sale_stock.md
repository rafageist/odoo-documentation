<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Product Availability

- Scope: Community Addons
- Source: odoo/addons/website_sale_stock
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Manage product inventory & availability

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 4
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 2
- Frontend asset files: 15

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
title Product Availability - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n4 views\n4 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n15 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_stock/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/website_sale_stock/Views|Views]] (4 files)
- Controllers: [[docs/Community Addons/website_sale_stock/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_sale_stock/Frontend|Frontend]] (15 files)

## Key models

- `product.combo`
- `product.feed`
- `product.product`
- `product.ribbon`
- `product.template`
- `res.config.settings`
- `sale.order`
- `sale.order.line`
- `stock.picking`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




