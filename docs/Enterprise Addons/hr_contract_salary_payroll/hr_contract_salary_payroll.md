<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Salary Configurator - Payroll

- Scope: Enterprise Addons
- Source: enterprise/hr_contract_salary_payroll
- Dependencies: [[docs/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Adds a Gross to Net Salary Simulaton

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 6
- Views: 8
- Actions: 2
- Menus: 6
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
- Frontend asset files: 5

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
title Salary Configurator - Payroll - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n8 views\n6 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_contract_salary_payroll/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/hr_contract_salary_payroll/Views|Views]] (6 files)
- Controllers: [[docs/Enterprise Addons/hr_contract_salary_payroll/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/hr_contract_salary_payroll/Frontend|Frontend]] (5 files)

## Key models

- `hr.applicant`
- `hr.contract.salary.benefit`
- `hr.contract.salary.offer`
- `hr.contract.salary.resume`
- `hr.employee`
- `hr.payroll.headcount.line`
- `hr.payslip.worked_days`
- `hr.version`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





