<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Accounting - MRP

- Scope: Community Addons
- Source: odoo/addons/mrp_account
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/stock_account/stock_account|stock_account]]

## Summary

Analytic accounting in Manufacturing

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 7
- Views: 9
- Actions: 4
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6
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
title Accounting - MRP - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n9 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mrp_account/Models|Models]] (17)
- Views and XML: [[docs/Community Addons/mrp_account/Views|Views]] (7 files)
- Frontend: [[docs/Community Addons/mrp_account/Frontend|Frontend]] (3 files)

## Key models

- `account.analytic.account`
- `account.analytic.applicability`
- `account.analytic.line`
- `account.move`
- `account.move.line`
- `mrp.account.wip.accounting`
- `mrp.account.wip.accounting.line`
- `mrp.production`
- `mrp.workcenter`
- `mrp.workcenter.productivity`
- `mrp.workorder`
- `product.category`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






