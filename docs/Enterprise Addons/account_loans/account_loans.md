<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Loans Management

- Scope: Enterprise Addons
- Source: enterprise/account_loans
- Dependencies: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]], [[docs/Community Addons/base_import/base_import|base_import]]

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 7
- Views: 15
- Actions: 4
- Menus: 2
- Rules (ir.rule): 2
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
title Loans Management - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n15 views\n7 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n2 rules\n6 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_loans/Models|Models]] (9)
- Views and XML: [[docs/Enterprise Addons/account_loans/Views|Views]] (7 files)
- Frontend: [[docs/Enterprise Addons/account_loans/Frontend|Frontend]] (3 files)

## Key models

- `account.asset`
- `account.asset.group`
- `account.journal`
- `account.loan`
- `account.loan.close.wizard`
- `account.loan.compute.wizard`
- `account.loan.line`
- `account.move`
- `account.return`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





