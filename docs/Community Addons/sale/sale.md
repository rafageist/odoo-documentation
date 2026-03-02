<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales

- Scope: Community Addons
- Source: odoo/addons/sale
- Dependencies: [[docs/Community Addons/sales_team/sales_team|sales_team]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/utm/utm|utm]]

## Summary

Sales internal machinery

## Generated coverage

- Models: 28
- XML files with UI/data artifacts: 24
- Views: 57
- Actions: 50
- Menus: 37
- Rules (ir.rule): 27
- Access CSV entries: 46
- Controller units: 4
- Frontend asset files: 53

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
title Sales - Generated Coverage
component "Module Overview" as overview
component "Models\n28" as models
component "Views / XML\n57 views\n24 files" as views
component "Controllers\n14 routes" as controllers
component "Frontend\n53 files" as frontend
component "Security / Data\n27 rules\n46 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/sale/Models|Models]] (28)
- Views and XML: [[docs/Community Addons/sale/Views|Views]] (24 files)
- Controllers: [[docs/Community Addons/sale/Controllers|Controllers]] (4)
- Frontend: [[docs/Community Addons/sale/Frontend|Frontend]] (53 files)

## Key models

- `account.analytic.applicability`
- `account.analytic.line`
- `account.chart.template`
- `account.invoice.report`
- `account.move`
- `account.move.line`
- `base.document.layout`
- `crm.team`
- `ir.actions.report`
- `ir.config_parameter`
- `payment.link.wizard`
- `payment.provider`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






