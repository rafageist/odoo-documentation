<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Mexico - Payroll CFDI

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_mx_hr_payroll_account_edi
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_mx_hr_payroll_account/l10n_mx_hr_payroll_account|l10n_mx_hr_payroll_account]], [[Odoo 19/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `HrPayrollStructure`
- `HrPayslip`
- `HrSalaryRule`
- `HrVersion`
- `HrWorkEntryType`
- `l10n.mx.concept`
- `L10nMxEdiDocument`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexico - Payroll CFDI - Models and Relations
class HrEmployee
class HrPayrollStructure
class HrPayslip
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
