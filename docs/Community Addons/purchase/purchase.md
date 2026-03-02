<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Purchase

- Scope: Community Addons
- Source: odoo/addons/purchase
- Dependencies: [[docs/Community Addons/account/account|account]]

## Summary

Purchase orders, tenders and agreements

## Generated coverage

- Models: 18
- XML files with UI/data artifacts: 13
- Views: 40
- Actions: 18
- Menus: 18
- Rules (ir.rule): 8
- Access CSV entries: 35
- Controller units: 1
- Frontend asset files: 23

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
title Purchase - Generated Coverage
component "Module Overview" as overview
component "Models\n18" as models
component "Views / XML\n40 views\n13 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n23 files" as frontend
component "Security / Data\n8 rules\n35 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/purchase/Models|Models]] (18)
- Views and XML: [[docs/Community Addons/purchase/Views|Views]] (13 files)
- Controllers: [[docs/Community Addons/purchase/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/purchase/Frontend|Frontend]] (23 files)

## Key models

- `account.analytic.account`
- `account.analytic.applicability`
- `account.move`
- `account.move.line`
- `account.tax`
- `bill.to.po.wizard`
- `ir.actions.report`
- `product.product`
- `product.supplierinfo`
- `product.template`
- `purchase.bill.line.match`
- `purchase.bill.union`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






