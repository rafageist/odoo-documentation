<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Purchase Stock

- Scope: Community Addons
- Source: odoo/addons/purchase_stock
- Dependencies: [[docs/Community Addons/stock_account/stock_account|stock_account]], [[docs/Community Addons/purchase/purchase|purchase]]

## Summary

Purchase Orders, Receipts, Vendor Bills for Stock

## Generated coverage

- Models: 27
- XML files with UI/data artifacts: 13
- Views: 21
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 14
- Controller units: 0
- Frontend asset files: 15

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
title Purchase Stock - Generated Coverage
component "Module Overview" as overview
component "Models\n27" as models
component "Views / XML\n21 views\n13 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n15 files" as frontend
component "Security / Data\n0 rules\n14 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/purchase_stock/Models|Models]] (27)
- Views and XML: [[docs/Community Addons/purchase_stock/Views|Views]] (13 files)
- Frontend: [[docs/Community Addons/purchase_stock/Frontend|Frontend]] (15 files)

## Key models

- `account.move`
- `account.move.line`
- `product.product`
- `product.replenish`
- `product.supplierinfo`
- `product.template`
- `purchase.order`
- `purchase.order.line`
- `purchase.report`
- `report.stock.report_stock_rule`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






