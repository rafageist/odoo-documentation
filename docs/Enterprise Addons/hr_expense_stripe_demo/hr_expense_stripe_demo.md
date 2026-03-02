<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Expense cards: Demo

- Scope: Enterprise Addons
- Source: enterprise/hr_expense_stripe_demo
- Dependencies: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]

## Summary

Create and manage company expense cards via Stripe: Demo

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 4
- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2
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
title Expense cards: Demo - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n5 views\n4 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_expense_stripe_demo/Models|Models]] (4)
- Views and XML: [[docs/Enterprise Addons/hr_expense_stripe_demo/Views|Views]] (4 files)

## Key models

- `hr.expense.stripe.card`
- `hr.expense.stripe.test.purchase.wizard`
- `hr.expense.stripe.test.shipping.wizard`
- `hr.expense.stripe.topup.wizard`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




