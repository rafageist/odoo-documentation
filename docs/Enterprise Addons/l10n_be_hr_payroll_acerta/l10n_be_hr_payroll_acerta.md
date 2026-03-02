<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Belgium - Payroll - Export to Acerta

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_hr_payroll_acerta
- Dependencies: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## Summary

Export Work Entries to Acerta

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `l10n.be.hr.payroll.export.acerta`
- `l10n.be.hr.payroll.export.acerta.employee`
- `HrVersion`
- `HrWorkEntryType`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Belgium - Payroll - Export to Acerta - Models and Relations
class "l10n.be.hr.payroll.export.acerta" as l10n_be_hr_payroll_export_acerta
class "l10n.be.hr.payroll.export.acerta.employee" as l10n_be_hr_payroll_export_acerta_employee
class HrVersion
class HrWorkEntryType
class ResCompany
l10n_be_hr_payroll_export_acerta --|> l10n_be_hr_payroll_export_acerta_employee : one2many
l10n_be_hr_payroll_export_acerta_employee --> l10n_be_hr_payroll_export_acerta : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



