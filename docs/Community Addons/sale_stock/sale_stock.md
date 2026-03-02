<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales and Warehouse Management

- Scope: Community Addons
- Source: odoo/addons/sale_stock
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Quotation, Sales Orders, Delivery & Invoicing Control

## Generated coverage

- Models: 22
- XML files with UI/data artifacts: 10
- Views: 14
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 16
- Controller units: 1
- Frontend asset files: 9

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
title Sales and Warehouse Management - Generated Coverage
component "Module Overview" as overview
component "Models\n22" as models
component "Views / XML\n14 views\n10 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n1 rules\n16 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/sale_stock/Models|Models]] (22)
- Views and XML: [[docs/Community Addons/sale_stock/Views|Views]] (10 files)
- Controllers: [[docs/Community Addons/sale_stock/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/sale_stock/Frontend|Frontend]] (9 files)

## Key models

- `account.move`
- `account.move.line`
- `product.template`
- `report.stock.report_stock_rule`
- `res.company`
- `res.config.settings`
- `res.users`
- `sale.order`
- `sale.order.line`
- `sale.report`
- `stock.forecasted_product_product`
- `stock.lot`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





