<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Mexico - Payroll CFDI

- Scope: Enterprise Addons
- Source: enterprise/l10n_mx_hr_payroll_account_edi
- Dependencies: [[docs/Enterprise Addons/l10n_mx_hr_payroll_account/l10n_mx_hr_payroll_account|l10n_mx_hr_payroll_account]], [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]

## XML Artifacts (detected)

- Views: 11
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `HrPayrollStructure`
- `HrPayslip`
- `HrPayslipRun`
- `HrSalaryRule`
- `HrVersion`
- `HrWorkEntryType`
- `l10n.mx.concept`
- `L10nMxEdiDocument`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Mexico - Payroll CFDI - Models and Relations
class HrEmployee
class HrPayrollStructure
class HrPayslip
class HrPayslipRun
class HrSalaryRule
class HrVersion
class HrWorkEntryType
class "l10n.mx.concept" as l10n_mx_concept
class L10nMxEdiDocument
class ResCompany
class "l10n_mx_edi.document" as l10n_mx_edi_document
HrPayslip --|> l10n_mx_edi_document : one2many
class "ir.attachment" as ir_attachment
HrPayslip --> ir_attachment : many2one
class "hr.payslip" as hr_payslip
HrPayslip --> hr_payslip : many2one
HrSalaryRule --> l10n_mx_concept : many2one
L10nMxEdiDocument --> hr_payslip : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




