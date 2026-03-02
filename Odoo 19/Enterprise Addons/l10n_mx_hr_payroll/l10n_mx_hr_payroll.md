<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Mexico - Payroll

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_mx_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 19/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `HrEmployee`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipWorkedDays`
- `HrVersion`
- `l10n.mx.hr.fonacot`
- `l10n.mx.hr.infonavit`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexico - Payroll - Models and Relations
class HrEmployee
class HrPayrollStructureType
class HrPayslip
class HrPayslipWorkedDays
class HrVersion
class "l10n.mx.hr.fonacot" as l10n_mx_hr_fonacot
class "l10n.mx.hr.infonavit" as l10n_mx_hr_infonavit
HrVersion --|> l10n_mx_hr_infonavit : one2many
HrVersion --|> l10n_mx_hr_fonacot : one2many
class "hr.version" as hr_version
l10n_mx_hr_fonacot --> hr_version : many2one
l10n_mx_hr_infonavit --> hr_version : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

