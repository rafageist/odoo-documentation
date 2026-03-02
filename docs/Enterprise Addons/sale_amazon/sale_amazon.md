<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Amazon Connector

- Scope: Enterprise Addons
- Source: enterprise/sale_amazon
- Dependencies: [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]

## Summary

Import Amazon orders and sync deliveries

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 10
- Views: 17
- Actions: 4
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 4
- Controller units: 1
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
title Amazon Connector - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n17 views\n10 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n2 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_amazon/Models|Models]] (12)
- Views and XML: [[docs/Enterprise Addons/sale_amazon/Views|Views]] (10 files)
- Controllers: [[docs/Enterprise Addons/sale_amazon/Controllers|Controllers]] (1)

## Key models

- `amazon.account`
- `amazon.marketplace`
- `amazon.offer`
- `amazon.recover.order.wizard`
- `product.product`
- `product.template`
- `res.config.settings`
- `res.partner`
- `sale.order`
- `sale.order.line`
- `stock.move`
- `stock.picking`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




