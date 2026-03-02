<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Resellers Commissions For Subscription

- Scope: Enterprise Addons
- Source: enterprise/partner_commission
- Dependencies: [[docs/Community Addons/purchase/purchase|purchase]], [[docs/Enterprise Addons/sale_subscription_partnership/sale_subscription_partnership|sale_subscription_partnership]], [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]

## Summary

Configure resellers commissions on subscription sale

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 10
- Views: 18
- Actions: 4
- Menus: 1
- Rules (ir.rule): 6
- Access CSV entries: 10
- Controller units: 0
- Frontend asset files: 0

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
title Resellers Commissions For Subscription - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n18 views\n10 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n6 rules\n10 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/partner_commission/Models|Models]] (15)
- Views and XML: [[docs/Enterprise Addons/partner_commission/Views|Views]] (10 files)

## Key models

- `account.move`
- `account.move.line`
- `commission.plan`
- `commission.rule`
- `crm.lead`
- `purchase.order`
- `res.company`
- `res.config.settings`
- `res.partner`
- `res.partner.grade`
- `sale.order`
- `sale.order.line`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




