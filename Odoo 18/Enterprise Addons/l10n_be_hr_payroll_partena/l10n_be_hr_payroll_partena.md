<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll - Export to Partena

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_partena
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to Partena

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.be.hr.payroll.export.partena`
- `l10n.be.hr.payroll.export.partena.employee`
- `HrWorkEntryType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to Partena - Models and Relations
class HrEmployee
class "l10n.be.hr.payroll.export.partena" as l10n_be_hr_payroll_export_partena
class "l10n.be.hr.payroll.export.partena.employee" as l10n_be_hr_payroll_export_partena_employee
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_partena --|> l10n_be_hr_payroll_export_partena_employee : one2many
l10n_be_hr_payroll_export_partena_employee --> l10n_be_hr_payroll_export_partena : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
