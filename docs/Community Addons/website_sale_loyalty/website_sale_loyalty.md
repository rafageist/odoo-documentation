<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Coupons, Promotions, Gift Card and Loyalty for eCommerce

- Scope: Community Addons
- Source: odoo/addons/website_sale_loyalty
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Community Addons/website_links/website_links|website_links]], [[docs/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

## Summary

Use coupon, promotion, gift cards and loyalty programs in your eCommerce store

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 5
- Views: 5
- Actions: 0
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 4
- Frontend asset files: 6

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
title Coupons, Promotions, Gift Card and Loyalty for eCommerce - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n5 views\n5 files" as views
component "Controllers\n7 routes" as controllers
component "Frontend\n6 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_loyalty/Models|Models]] (7)
- Views and XML: [[docs/Community Addons/website_sale_loyalty/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/website_sale_loyalty/Controllers|Controllers]] (4)
- Frontend: [[docs/Community Addons/website_sale_loyalty/Frontend|Frontend]] (6 files)

## Key models

- `coupon.share`
- `loyalty.card`
- `loyalty.program`
- `loyalty.rule`
- `product.product`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




