<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Delivery - Stock

- Scope: Community Addons
- Source: odoo/addons/stock_delivery
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/delivery/delivery|delivery]]

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 8
- Views: 16
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 5
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
title Delivery - Stock - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n16 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/stock_delivery/Models|Models]] (13)
- Views and XML: [[docs/Community Addons/stock_delivery/Views|Views]] (8 files)

## Key models

- `choose.delivery.carrier`
- `delivery.carrier`
- `product.template`
- `sale.order`
- `sale.order.line`
- `stock.move`
- `stock.move.line`
- `stock.package`
- `stock.package.type`
- `stock.picking`
- `stock.put.in.pack`
- `stock.return.picking`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






