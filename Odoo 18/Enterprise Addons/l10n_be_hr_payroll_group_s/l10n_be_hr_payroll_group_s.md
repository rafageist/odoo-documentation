<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll - Export to Group S

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll_group_s
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to Group S

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrContract`
- `l10n.be.hr.payroll.export.group.s`
- `l10n.be.hr.payroll.export.group.s.employee`
- `HrWorkEntryType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to Group S - Models and Relations
class HrContract
class "l10n.be.hr.payroll.export.group.s" as l10n_be_hr_payroll_export_group_s
class "l10n.be.hr.payroll.export.group.s.employee" as l10n_be_hr_payroll_export_group_s_employee
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_group_s --|> l10n_be_hr_payroll_export_group_s_employee : one2many
l10n_be_hr_payroll_export_group_s_employee --> l10n_be_hr_payroll_export_group_s : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
