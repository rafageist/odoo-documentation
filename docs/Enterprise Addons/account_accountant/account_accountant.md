<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Invoicing

- Scope: Enterprise Addons
- Source: enterprise/account_accountant
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[docs/Community Addons/web_tour/web_tour|web_tour]]

## Summary

Invoices, Payments, Follow-ups & Bank synchronization (Enterprise)

## Generated coverage

- Models: 20
- XML files with UI/data artifacts: 14
- Views: 33
- Actions: 14
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 8
- Controller units: 0
- Frontend asset files: 46

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
component "Models\n20" as models
component "Views / XML\n33 views\n14 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n46 files" as frontend
component "Security / Data\n0 rules\n8 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_accountant/Models|Models]] (20)
- Views and XML: [[docs/Enterprise Addons/account_accountant/Views|Views]] (14 files)
- Frontend: [[docs/Enterprise Addons/account_accountant/Frontend|Frontend]] (46 files)

## Key models

- `account.account`
- `account.auto.reconcile.wizard`
- `account.bank.statement`
- `account.bank.statement.line`
- `account.change.lock.date`
- `account.chart.template`
- `account.fiscal.year`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.payment`
- `account.reconcile.model`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





