<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Invoicing

- Scope: Community Addons
- Source: odoo/addons/account
- Dependencies: [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/onboarding/onboarding|onboarding]], [[docs/Community Addons/product/product|product]], [[docs/Community Addons/analytic/analytic|analytic]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/digest/digest|digest]]

## Summary

Invoices & Payments

## Generated coverage

- Models: 85
- XML files with UI/data artifacts: 52
- Views: 146
- Actions: 80
- Menus: 53
- Rules (ir.rule): 31
- Access CSV entries: 145
- Controller units: 5
- Frontend asset files: 114

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
title Invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n85" as models
component "Views / XML\n146 views\n52 files" as views
component "Controllers\n11 routes" as controllers
component "Frontend\n114 files" as frontend
component "Security / Data\n31 rules\n145 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/account/Models|Models]] (85)
- Views and XML: [[docs/Community Addons/account/Views|Views]] (52 files)
- Controllers: [[docs/Community Addons/account/Controllers|Controllers]] (5)
- Frontend: [[docs/Community Addons/account/Frontend|Frontend]] (114 files)

## Key models

- `account.account`
- `account.account.tag`
- `account.accrued.orders.wizard`
- `account.analytic.account`
- `account.analytic.applicability`
- `account.analytic.distribution.model`
- `account.analytic.line`
- `account.automatic.entry.wizard`
- `account.autopost.bills.wizard`
- `account.bank.statement`
- `account.bank.statement.line`
- `account.cash.rounding`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






