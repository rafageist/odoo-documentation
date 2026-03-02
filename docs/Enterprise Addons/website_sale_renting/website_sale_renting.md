<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# eCommerce Rental

- Scope: Enterprise Addons
- Source: enterprise/website_sale_renting
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]], [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]

## Summary

Sell rental products on your eCommerce

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 3
- Controller units: 5
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
title eCommerce Rental - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n11 routes" as controllers
component "Frontend\n8 files" as frontend
component "Security / Data\n1 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_sale_renting/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/website_sale_renting/Views|Views]] (3 files)
- Controllers: [[docs/Enterprise Addons/website_sale_renting/Controllers|Controllers]] (5)
- Frontend: [[docs/Enterprise Addons/website_sale_renting/Frontend|Frontend]] (8 files)

## Key models

- `product.pricelist`
- `product.product`
- `product.template`
- `res.company`
- `res.config.settings`
- `sale.order`
- `sale.order.line`
- `website`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




