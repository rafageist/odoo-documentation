<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Online Bank Statement Synchronization

- Scope: Enterprise Addons
- Source: enterprise/account_online_synchronization
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

This module is used for Online bank synchronization.

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 9
- Views: 13
- Actions: 1
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 11
- Controller units: 2
- Frontend asset files: 27

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
title Online Bank Statement Synchronization - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n13 views\n9 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n27 files" as frontend
component "Security / Data\n2 rules\n11 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_online_synchronization/Models|Models]] (10)
- Views and XML: [[docs/Enterprise Addons/account_online_synchronization/Views|Views]] (9 files)
- Controllers: [[docs/Enterprise Addons/account_online_synchronization/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/account_online_synchronization/Frontend|Frontend]] (27 files)

## Key models

- `account.bank.selection`
- `account.bank.statement.line`
- `account.bank.statement.line.transient`
- `account.duplicate.transaction.wizard`
- `account.journal`
- `account.missing.transaction.wizard`
- `account.online.account`
- `account.online.link`
- `res.company`
- `res.partner`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




