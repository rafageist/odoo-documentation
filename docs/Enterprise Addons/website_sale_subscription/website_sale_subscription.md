<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# eCommerce Subscription

- Scope: Enterprise Addons
- Source: enterprise/website_sale_subscription
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]

## Summary

Sell subscription products on your eCommerce

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
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
title eCommerce Subscription - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_sale_subscription/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/website_sale_subscription/Views|Views]] (1 files)
- Controllers: [[docs/Enterprise Addons/website_sale_subscription/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/website_sale_subscription/Frontend|Frontend]] (4 files)

## Key models

- `product.product`
- `product.template`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




