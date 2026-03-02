<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Indian Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_in_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Generated coverage

- Models: 19
- XML files with UI/data artifacts: 13
- Views: 15
- Actions: 12
- Menus: 7
- Rules (ir.rule): 0
- Access CSV entries: 8
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
title Indian Payroll - Generated Coverage
component "Module Overview" as overview
component "Models\n19" as models
component "Views / XML\n15 views\n13 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n8 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_in_hr_payroll/Models|Models]] (19)
- Views and XML: [[docs/Enterprise Addons/l10n_in_hr_payroll/Views|Views]] (13 files)

## Key models

- `hr.employee`
- `hr.payroll.payment.report.wizard`
- `hr.payroll.structure.type`
- `hr.payslip`
- `hr.payslip.run`
- `hr.version`
- `l10n.in.hr.payroll.epf.report`
- `l10n.in.hr.payroll.esic.report`
- `l10n.in.labour.welfare.fund.line.wizard`
- `l10n.in.labour.welfare.fund.wizard`
- `l10n.in.tds.computation.wizard`
- `l10n_in_hr_payroll.salary.statement`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




