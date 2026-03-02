<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Shopper's Wishlist

- Scope: Community Addons
- Source: odoo/addons/website_sale_wishlist
- Dependencies: [[docs/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allow shoppers to enlist products

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 1
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 4
- Controller units: 2
- Frontend asset files: 11

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
title Shopper's Wishlist - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n0 views\n1 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n11 files" as frontend
component "Security / Data\n2 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_wishlist/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/website_sale_wishlist/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/website_sale_wishlist/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_sale_wishlist/Frontend|Frontend]] (11 files)

## Key models

- `product.product`
- `product.template`
- `product.wishlist`
- `res.partner`
- `res.users`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




