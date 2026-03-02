<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Payment - Account

- Scope: Community Addons
- Source: odoo/addons/account_payment
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/payment/payment|payment]]

## Summary

Enable customers to pay invoices on the portal and post payments when transactions are processed.

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 11
- Views: 9
- Actions: 1
- Menus: 4
- Rules (ir.rule): 1
- Access CSV entries: 3
- Controller units: 2
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
title Payment - Account - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n9 views\n11 files" as views
component "Controllers\n5 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n1 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/account_payment/Models|Models]] (11)
- Views and XML: [[docs/Community Addons/account_payment/Views|Views]] (11 files)
- Controllers: [[docs/Community Addons/account_payment/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/account_payment/Frontend|Frontend]] (3 files)

## Key models

- `account.journal`
- `account.move`
- `account.payment`
- `account.payment.method`
- `account.payment.method.line`
- `account.payment.register`
- `payment.link.wizard`
- `payment.provider`
- `payment.refund.wizard`
- `payment.transaction`
- `res.config.settings`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






