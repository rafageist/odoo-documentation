<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Subscriptions

- Scope: Enterprise Addons
- Source: enterprise/sale_subscription
- Dependencies: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/portal/portal|portal]], [[docs/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[docs/Community Addons/rating/rating|rating]], [[docs/Community Addons/sms/sms|sms]]

## Summary

Generate recurring invoices and manage renewals

## Generated coverage

- Models: 27
- XML files with UI/data artifacts: 22
- Views: 53
- Actions: 45
- Menus: 22
- Rules (ir.rule): 9
- Access CSV entries: 19
- Controller units: 2
- Frontend asset files: 13

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
title Subscriptions - Generated Coverage
component "Module Overview" as overview
component "Models\n27" as models
component "Views / XML\n53 views\n22 files" as views
component "Controllers\n16 routes" as controllers
component "Frontend\n13 files" as frontend
component "Security / Data\n9 rules\n19 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/sale_subscription/Models|Models]] (27)
- Views and XML: [[docs/Enterprise Addons/sale_subscription/Views|Views]] (22 files)
- Controllers: [[docs/Enterprise Addons/sale_subscription/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/sale_subscription/Frontend|Frontend]] (13 files)

## Key models

- `account.move`
- `account.move.line`
- `account.move.send`
- `ir.http`
- `payment.link.wizard`
- `payment.provider`
- `payment.token`
- `payment.transaction`
- `product.pricelist`
- `product.pricelist.item`
- `product.product`
- `product.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




