<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Delivery Costs

- Scope: Community Addons
- Source: odoo/addons/delivery
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/payment_custom/payment_custom|payment_custom]]

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 10
- Views: 12
- Actions: 2
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 10
- Controller units: 1
- Frontend asset files: 13

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
title Delivery Costs - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n12 views\n10 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n13 files" as frontend
component "Security / Data\n1 rules\n10 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/delivery/Models|Models]] (12)
- Views and XML: [[docs/Community Addons/delivery/Views|Views]] (10 files)
- Controllers: [[docs/Community Addons/delivery/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/delivery/Frontend|Frontend]] (13 files)

## Key models

- `choose.delivery.carrier`
- `delivery.carrier`
- `delivery.price.rule`
- `delivery.zip.prefix`
- `ir.http`
- `ir.module.module`
- `payment.provider`
- `payment.transaction`
- `product.category`
- `res.partner`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






