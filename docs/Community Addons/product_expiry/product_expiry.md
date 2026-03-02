<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Products Expiration Date

- Scope: Community Addons
- Source: odoo/addons/product_expiry
- Dependencies: [[docs/Community Addons/stock/stock|stock]]

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 6
- Views: 14
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 3

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
title Products Expiration Date - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n14 views\n6 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/product_expiry/Models|Models]] (12)
- Views and XML: [[docs/Community Addons/product_expiry/Views|Views]] (6 files)
- Frontend: [[docs/Community Addons/product_expiry/Frontend|Frontend]] (3 files)

## Key models

- `expiry.picking.confirmation`
- `product.product`
- `product.template`
- `report.stock.quantity`
- `res.config.settings`
- `stock.forecasted_product_product`
- `stock.lot`
- `stock.move`
- `stock.move.line`
- `stock.picking`
- `stock.quant`
- `stock.rule`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






