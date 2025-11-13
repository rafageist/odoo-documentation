<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Payroll - Export to Group S

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_be_hr_payroll_group_s
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to Group S

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.be.hr.payroll.export.group.s`
- `l10n.be.hr.payroll.export.group.s.employee`
- `HrVersion`
- `HrWorkEntryType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to Group S - Models and Relations
class HrEmployee
class "l10n.be.hr.payroll.export.group.s" as l10n_be_hr_payroll_export_group_s
class "l10n.be.hr.payroll.export.group.s.employee" as l10n_be_hr_payroll_export_group_s_employee
class HrVersion
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_group_s --|> l10n_be_hr_payroll_export_group_s_employee : one2many
l10n_be_hr_payroll_export_group_s_employee --> l10n_be_hr_payroll_export_group_s : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
