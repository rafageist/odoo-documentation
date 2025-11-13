<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Payroll - Export to Prisma

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_be_hr_payroll_prisma
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to Prisma

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.be.hr.payroll.export.prisma`
- `l10n.be.hr.payroll.export.prisma.employee`
- `HrWorkEntryType`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to Prisma - Models and Relations
class HrEmployee
class "l10n.be.hr.payroll.export.prisma" as l10n_be_hr_payroll_export_prisma
class "l10n.be.hr.payroll.export.prisma.employee" as l10n_be_hr_payroll_export_prisma_employee
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_prisma --|> l10n_be_hr_payroll_export_prisma_employee : one2many
l10n_be_hr_payroll_export_prisma_employee --> l10n_be_hr_payroll_export_prisma : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
