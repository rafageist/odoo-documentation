<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Rental Stock Management

- Scope: Enterprise Addons
- Source: enterprise/sale_stock_renting
- Dependencies: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Allows use of stock application to manage rentals inventory

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 9
- Views: 12
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 2

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
title Rental Stock Management - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n12 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_stock_renting/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/sale_stock_renting/Views|Views]] (9 files)
- Frontend: [[docs/Enterprise Addons/sale_stock_renting/Frontend|Frontend]] (2 files)

## Key models

- `account.move`
- `account.move.line`
- `product.product`
- `product.template`
- `rental.order.wizard`
- `rental.order.wizard.line`
- `res.company`
- `res.config.settings`
- `sale.order`
- `sale.order.line`
- `sale.rental.report`
- `stock.lot`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





