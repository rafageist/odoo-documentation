<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Drop Shipping

- Scope: Community Addons
- Source: odoo/addons/stock_dropshipping
- Dependencies: [[docs/Community Addons/sale_purchase_stock/sale_purchase_stock|sale_purchase_stock]]

## Summary

Drop Shipping

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
- Frontend asset files: 0

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
title Drop Shipping - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/stock_dropshipping/Models|Models]] (11)
- Views and XML: [[docs/Community Addons/stock_dropshipping/Views|Views]] (3 files)

## Key models

- `product.product`
- `purchase.order`
- `res.company`
- `sale.order`
- `sale.order.line`
- `stock.lot`
- `stock.move`
- `stock.picking`
- `stock.picking.type`
- `stock.replenish.mixin`
- `stock.rule`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





