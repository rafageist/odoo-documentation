<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Payroll - Export to SD Worx

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_hr_payroll_sd_worx
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to SD Worx

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.be.hr.payroll.export.sdworx`
- `l10n.be.hr.payroll.export.sdworx.employee`
- `HrWorkEntryType`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Export to SD Worx - Models and Relations
class HrEmployee
class "l10n.be.hr.payroll.export.sdworx" as l10n_be_hr_payroll_export_sdworx
class "l10n.be.hr.payroll.export.sdworx.employee" as l10n_be_hr_payroll_export_sdworx_employee
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_sdworx --|> l10n_be_hr_payroll_export_sdworx_employee : one2many
l10n_be_hr_payroll_export_sdworx_employee --> l10n_be_hr_payroll_export_sdworx : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

