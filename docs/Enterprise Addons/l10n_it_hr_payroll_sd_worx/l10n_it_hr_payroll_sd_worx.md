<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Italy - Payroll - Export to SD Worx

- Scope: Enterprise Addons
- Source: enterprise/l10n_it_hr_payroll_sd_worx
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Export Work Entries to SD Worx

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `l10n.it.hr.payroll.export.sdworx`
- `l10n.it.hr.payroll.export.sdworx.employee`
- `HrWorkEntryType`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Italy - Payroll - Export to SD Worx - Models and Relations
class HrEmployee
class "l10n.it.hr.payroll.export.sdworx" as l10n_it_hr_payroll_export_sdworx
class "l10n.it.hr.payroll.export.sdworx.employee" as l10n_it_hr_payroll_export_sdworx_employee
class HrWorkEntryType
class ResCompany
l10n_it_hr_payroll_export_sdworx --|> l10n_it_hr_payroll_export_sdworx_employee : one2many
l10n_it_hr_payroll_export_sdworx_employee --> l10n_it_hr_payroll_export_sdworx : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



