<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Fiscal Categories on Fleets

- Scope: Enterprise Addons
- Source: enterprise/account_fiscal_categories_fleet
- Dependencies: [[docs/Enterprise Addons/account_accountant_fleet/account_accountant_fleet|account_accountant_fleet]], [[docs/Enterprise Addons/account_fiscal_categories/account_fiscal_categories|account_fiscal_categories]]

## Summary

Manage fiscal categories with fleets

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 2
- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3
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
title Fiscal Categories on Fleets - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n3 views\n2 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_fiscal_categories_fleet/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/account_fiscal_categories_fleet/Views|Views]] (2 files)
- Frontend: [[docs/Enterprise Addons/account_fiscal_categories_fleet/Frontend|Frontend]] (3 files)

## Key models

- `account.deferred.report.handler`
- `account.fiscal.categories.fleet.report.handler`
- `account.fiscal.category`
- `account.move.line`
- `fleet.disallowed.expenses.rate`
- `fleet.vehicle`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




