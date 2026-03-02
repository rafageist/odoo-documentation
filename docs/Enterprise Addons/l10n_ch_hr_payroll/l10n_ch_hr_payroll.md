<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Switzerland - Swissdec Certified ELM 5.0 - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_ch_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Community Addons/iap/iap|iap]]

## Generated coverage

- Models: 65
- XML files with UI/data artifacts: 45
- Views: 78
- Actions: 33
- Menus: 34
- Rules (ir.rule): 18
- Access CSV entries: 54
- Controller units: 0
- Frontend asset files: 12

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
title Switzerland - Swissdec Certified ELM 5.0 - Payroll - Generated Coverage
component "Module Overview" as overview
component "Models\n65" as models
component "Views / XML\n78 views\n45 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n12 files" as frontend
component "Security / Data\n18 rules\n54 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ch_hr_payroll/Models|Models]] (65)
- Views and XML: [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views|Views]] (45 files)
- Frontend: [[docs/Enterprise Addons/l10n_ch_hr_payroll/Frontend|Frontend]] (12 files)

## Key models

- `ch.yearly.report`
- `hr.employee`
- `hr.employee.is.line`
- `hr.employee.is.line.correction`
- `hr.leave`
- `hr.leave.type`
- `hr.payslip`
- `hr.payslip.is.log.line`
- `hr.payslip.run`
- `hr.rule.parameter`
- `hr.salary.rule`
- `hr.version`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




