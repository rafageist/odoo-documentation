<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payment Provider: Sepa Direct Debit

- Scope: Enterprise Addons
- Source: enterprise/payment_sepa_direct_debit
- Dependencies: [[docs/Enterprise Addons/account_sepa_direct_debit/account_sepa_direct_debit|account_sepa_direct_debit]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/payment_custom/payment_custom|payment_custom]]

## Summary

A payment provider for enabling Sepa Direct Debit in the EU.

## Generated coverage

- Models: 7
- XML files with UI/data artifacts: 2
- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 1

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
title Payment Provider: Sepa Direct Debit - Generated Coverage
component "Module Overview" as overview
component "Models\n7" as models
component "Views / XML\n3 views\n2 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/payment_sepa_direct_debit/Models|Models]] (7)
- Views and XML: [[docs/Enterprise Addons/payment_sepa_direct_debit/Views|Views]] (2 files)
- Controllers: [[docs/Enterprise Addons/payment_sepa_direct_debit/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/payment_sepa_direct_debit/Frontend|Frontend]] (1 files)

## Key models

- `account.bank.statement.line`
- `account.payment.method`
- `payment.provider`
- `payment.token`
- `payment.transaction`
- `res.partner`
- `sdd.mandate`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





