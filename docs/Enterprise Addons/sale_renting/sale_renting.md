<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Rental

- Scope: Enterprise Addons
- Source: enterprise/sale_renting
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Enterprise Addons/web_gantt/web_gantt|web_gantt]]

## Summary

Manage rental contracts, deliveries and returns

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 12
- Views: 26
- Actions: 25
- Menus: 13
- Rules (ir.rule): 1
- Access CSV entries: 11
- Controller units: 2
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
title Rental - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n26 views\n12 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n7 files" as frontend
component "Security / Data\n1 rules\n11 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_renting/Models|Models]] (12)
- Views and XML: [[docs/Enterprise Addons/sale_renting/Views|Views]] (12 files)
- Controllers: [[docs/Enterprise Addons/sale_renting/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/sale_renting/Frontend|Frontend]] (7 files)

## Key models

- `product.pricelist`
- `product.pricing`
- `product.product`
- `product.template`
- `rental.order.wizard`
- `rental.order.wizard.line`
- `res.company`
- `res.config.settings`
- `sale.order`
- `sale.order.line`
- `sale.rental.report`
- `sale.temporal.recurrence`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





