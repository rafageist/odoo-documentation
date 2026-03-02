<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# WMS Accounting

- Scope: Community Addons
- Source: odoo/addons/stock_account
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/account/account|account]]

## Summary

Inventory, Logistic, Valuation, Accounting

## Generated coverage

- Models: 24
- XML files with UI/data artifacts: 14
- Views: 19
- Actions: 5
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 9
- Controller units: 0
- Frontend asset files: 18

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
title WMS Accounting - Generated Coverage
component "Module Overview" as overview
component "Models\n24" as models
component "Views / XML\n19 views\n14 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n18 files" as frontend
component "Security / Data\n2 rules\n9 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/stock_account/Models|Models]] (24)
- Views and XML: [[docs/Community Addons/stock_account/Views|Views]] (14 files)
- Frontend: [[docs/Community Addons/stock_account/Frontend|Frontend]] (18 files)

## Key models

- `account.account`
- `account.analytic.account`
- `account.analytic.plan`
- `account.chart.template`
- `account.move`
- `account.move.line`
- `product.category`
- `product.product`
- `product.template`
- `product.value`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






