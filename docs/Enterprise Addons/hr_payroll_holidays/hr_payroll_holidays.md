<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Time Off in Payslips

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll_holidays
- Dependencies: [[docs/Enterprise Addons/hr_holidays_gantt/hr_holidays_gantt|hr_holidays_gantt]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 4
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title Time Off in Payslips - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/hr_payroll_holidays/Models|Models]] (8)
- Views and XML: [[docs/Enterprise Addons/hr_payroll_holidays/Views|Views]] (3 files)

## Key models

- `hr.employee`
- `hr.leave`
- `hr.payslip`
- `hr.version`
- `mail.activity`
- `mail.activity.type`
- `res.company`
- `res.config.settings`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




