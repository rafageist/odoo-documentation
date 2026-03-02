<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Salary Configurator

- Scope: Enterprise Addons
- Source: enterprise/hr_contract_salary
- Dependencies: [[docs/Enterprise Addons/hr_sign/hr_sign|hr_sign]], [[docs/Community Addons/http_routing/http_routing|http_routing]], [[docs/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]], [[docs/Enterprise Addons/sign/sign|sign]]

## Summary

Sign Employment Contracts

## Generated coverage

- Models: 23
- XML files with UI/data artifacts: 16
- Views: 27
- Actions: 12
- Menus: 10
- Rules (ir.rule): 4
- Access CSV entries: 43
- Controller units: 2
- Frontend asset files: 10

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
title Salary Configurator - Generated Coverage
component "Module Overview" as overview
component "Models\n23" as models
component "Views / XML\n27 views\n16 files" as views
component "Controllers\n9 routes" as controllers
component "Frontend\n10 files" as frontend
component "Security / Data\n4 rules\n43 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_contract_salary/Models|Models]] (23)
- Views and XML: [[docs/Enterprise Addons/hr_contract_salary/Views|Views]] (16 files)
- Controllers: [[docs/Enterprise Addons/hr_contract_salary/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/hr_contract_salary/Frontend|Frontend]] (10 files)

## Key models

- `hr.applicant`
- `hr.contract.recruitment.report`
- `hr.contract.salary.benefit`
- `hr.contract.salary.benefit.type`
- `hr.contract.salary.benefit.value`
- `hr.contract.salary.offer`
- `hr.contract.salary.offer.refusal.reason`
- `hr.contract.salary.personal.info`
- `hr.contract.salary.personal.info.type`
- `hr.contract.salary.personal.info.value`
- `hr.contract.salary.resume`
- `hr.contract.salary.resume.category`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




