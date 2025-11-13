<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll - Export to UCM

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_ucm
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to UCM

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.be.hr.payroll.export.ucm`
- `l10n.be.hr.payroll.export.ucm.employee`
- `HrWorkEntryType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to UCM - Models and Relations
class HrEmployee
class "l10n.be.hr.payroll.export.ucm" as l10n_be_hr_payroll_export_ucm
class "l10n.be.hr.payroll.export.ucm.employee" as l10n_be_hr_payroll_export_ucm_employee
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_ucm --|> l10n_be_hr_payroll_export_ucm_employee : one2many
l10n_be_hr_payroll_export_ucm_employee --> l10n_be_hr_payroll_export_ucm : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
