<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Expense cards

- Scope: Enterprise Addons
- Source: enterprise/hr_expense_stripe
- Dependencies: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Create and manage company expense cards via Stripe

## Generated coverage

- Models: 19
- XML files with UI/data artifacts: 12
- Views: 17
- Actions: 2
- Menus: 2
- Rules (ir.rule): 5
- Access CSV entries: 10
- Controller units: 1
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
title Expense cards - Generated Coverage
component "Module Overview" as overview
component "Models\n19" as models
component "Views / XML\n17 views\n12 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n13 files" as frontend
component "Security / Data\n5 rules\n10 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_expense_stripe/Models|Models]] (19)
- Views and XML: [[docs/Enterprise Addons/hr_expense_stripe/Views|Views]] (12 files)
- Controllers: [[docs/Enterprise Addons/hr_expense_stripe/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/hr_expense_stripe/Frontend|Frontend]] (13 files)

## Key models

- `account.bank.statement.line`
- `account.chart.template`
- `account.journal`
- `account.payment`
- `account.payment.method.line`
- `account.payment.register`
- `hr.employee`
- `hr.expense`
- `hr.expense.split`
- `hr.expense.stripe.card`
- `hr.expense.stripe.card.block.wizard`
- `hr.expense.stripe.card.receive.wizard`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




