
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Payroll

- Scope: Enterprise Addons
- Source: enterprise/documents_hr_payroll
- Dependencies: [[docs/Enterprise Addons/documents_hr/documents_hr|documents_hr]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Store employee payslips in the Document app

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 4
- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 0
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
title Documents - Payroll - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n3 views\n4 files" as views
component "Controllers\n0 routes" as controllers
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

- Models: [[docs/Enterprise Addons/documents_hr_payroll/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/documents_hr_payroll/Views|Views]] (4 files)
- Frontend: [[docs/Enterprise Addons/documents_hr_payroll/Frontend|Frontend]] (5 files)

## Key models

- `hr.employee`
- `hr.payroll.declaration.mixin`
- `hr.payroll.employee.declaration`
- `hr.payslip`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




