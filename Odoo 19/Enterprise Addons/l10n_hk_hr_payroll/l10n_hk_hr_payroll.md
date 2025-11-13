<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Hong Kong - Payroll

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_hk_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 19/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
## XML Artifacts (detected)

- Views: 25
- Actions: 12
- Menus: 6
- Rules (ir.rule): 0
- Access CSV entries: 10

## Detected Models

- `HrDepartureReason`
- `HrEmployee`
- `HrPayrollEmployeeDeclaration`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipRun`
- `HrPayslipWorkedDays`
- `HrVersion`
- `HrWorkEntryType`
- `l10n_hk.ir56b`
- `l10n_hk.ir56e`
- `l10n_hk.ir56f`
- `l10n_hk.ir56g`
- `l10n_hk.ir56g.line`
- `l10n_hk.manulife.mpf`
- `l10n_hk.manulife.mpf.line`
- `l10n_hk.rental`
- `ResourceCalendar`
- `ResBank`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Hong Kong - Payroll - Models and Relations
class HrDepartureReason
class HrEmployee
class HrPayrollEmployeeDeclaration
class HrPayrollStructureType
class HrPayslip
class HrPayslipRun
class HrPayslipWorkedDays
class HrVersion
class HrWorkEntryType
class "l10n_hk.ir56b" as l10n_hk_ir56b
class "l10n_hk.ir56e" as l10n_hk_ir56e
class "l10n_hk.ir56f" as l10n_hk_ir56f
class "l10n_hk.ir56g" as l10n_hk_ir56g
class "l10n_hk.ir56g.line" as l10n_hk_ir56g_line
class "l10n_hk.manulife.mpf" as l10n_hk_manulife_mpf
class "l10n_hk.manulife.mpf.line" as l10n_hk_manulife_mpf_line
class "l10n_hk.rental" as l10n_hk_rental
class ResourceCalendar
class ResBank
class ResCompany
HrEmployee --|> l10n_hk_rental : one2many
class "hr.leave" as hr_leave
HrPayslipWorkedDays --> hr_leave : many2one
HrVersion --> l10n_hk_rental : many2one
l10n_hk_ir56g --|> l10n_hk_ir56g_line : one2many
class "hr.employee" as hr_employee
l10n_hk_ir56g_line --> hr_employee : many2one
l10n_hk_ir56g_line --> l10n_hk_ir56g : many2one
class "res.company" as res_company
l10n_hk_manulife_mpf --> res_company : many2one
class "res.currency" as res_currency
l10n_hk_manulife_mpf --> res_currency : many2one
l10n_hk_manulife_mpf --|> l10n_hk_manulife_mpf_line : one2many
class "ir.attachment" as ir_attachment
l10n_hk_manulife_mpf --> ir_attachment : many2one
l10n_hk_manulife_mpf_line --> hr_employee : many2one
l10n_hk_manulife_mpf_line --> res_currency : many2one
l10n_hk_manulife_mpf_line --> l10n_hk_manulife_mpf : many2one
l10n_hk_rental --> hr_employee : many2one
l10n_hk_rental --> res_company : many2one
class "res.partner.bank" as res_partner_bank
ResCompany --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
