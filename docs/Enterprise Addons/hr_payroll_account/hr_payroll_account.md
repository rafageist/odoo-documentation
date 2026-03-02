<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payroll Accounting

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll_account
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Enterprise Addons/accountant/accountant|accountant]], [[docs/Community Addons/base_iban/base_iban|base_iban]]

## Generated coverage

- Models: 16
- XML files with UI/data artifacts: 9
- Views: 12
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
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
title Payroll Accounting - Generated Coverage
component "Module Overview" as overview
component "Models\n16" as models
component "Views / XML\n12 views\n9 files" as views
component "Controllers\n0 routes" as controllers
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

- Models: [[docs/Enterprise Addons/hr_payroll_account/Models|Models]] (16)
- Views and XML: [[docs/Enterprise Addons/hr_payroll_account/Views|Views]] (9 files)
- Frontend: [[docs/Enterprise Addons/hr_payroll_account/Frontend|Frontend]] (1 files)

## Key models

- `account.chart.template`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.payment`
- `account.payment.register`
- `hr.payroll.payment.report.wizard`
- `hr.payroll.structure`
- `hr.payslip`
- `hr.payslip.line`
- `hr.payslip.run`
- `hr.salary.rule`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




