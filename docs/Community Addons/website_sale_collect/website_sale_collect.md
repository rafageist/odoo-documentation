
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Click & Collect

- Scope: Community Addons
- Source: odoo/addons/website_sale_collect
- Dependencies: [[docs/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]], [[docs/Community Addons/payment_custom/payment_custom|payment_custom]], [[docs/Community Addons/website_sale_stock/website_sale_stock|website_sale_stock]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 4
- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 10

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
title Click & Collect - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n4 views\n4 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n10 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale_collect/Models|Models]] (8)
- Views and XML: [[docs/Community Addons/website_sale_collect/Views|Views]] (4 files)
- Controllers: [[docs/Community Addons/website_sale_collect/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/website_sale_collect/Frontend|Frontend]] (10 files)

## Key models

- `delivery.carrier`
- `payment.provider`
- `payment.transaction`
- `product.template`
- `res.config.settings`
- `sale.order`
- `stock.warehouse`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


