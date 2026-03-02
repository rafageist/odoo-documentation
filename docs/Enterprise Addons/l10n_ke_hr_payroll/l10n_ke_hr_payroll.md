<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Kenya - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_ke_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 9
- Views: 6
- Actions: 6
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 5
- Controller units: 1
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
title Kenya - Payroll - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n6 views\n9 files" as views
component "Controllers\n3 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n2 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_ke_hr_payroll/Models|Models]] (13)
- Views and XML: [[docs/Enterprise Addons/l10n_ke_hr_payroll/Views|Views]] (9 files)
- Controllers: [[docs/Enterprise Addons/l10n_ke_hr_payroll/Controllers|Controllers]] (1)

## Key models

- `hr.employee`
- `hr.payroll.structure.type`
- `hr.payslip`
- `hr.payslip.line`
- `hr.version`
- `ir.ui.menu`
- `l10n.ke.hr.payroll.nssf.report.line.wizard`
- `l10n.ke.hr.payroll.nssf.report.wizard`
- `l10n.ke.hr.payroll.shif.report.line.wizard`
- `l10n.ke.hr.payroll.shif.report.wizard`
- `l10n_ke.tax.deduction.card`
- `report.l10n_ke_hr_payroll.report_tax_deduction_card`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




